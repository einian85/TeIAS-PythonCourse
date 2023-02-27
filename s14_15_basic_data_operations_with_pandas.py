# -*- coding: utf-8 -*-
"""S14_15-Basic Data Operations with pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xMsoqdvjaY9WKFbMwyVp0Nd6qjj2v2ys

# Basic Data Operations with `pandas`

* DataFrame
* Importing Data
* Select Subsets
  * Subset of variables
  * Subset of records by index
  * Subset of records by condition
* Sort
* Add New Variables
* Reshaping Data 
  * Wide to Long
  * Long to Wide
* Renaming columns
* Summarizing
* Summarizing in Groups
* Binding and Merging Data

## `DataFrame`
`DataFrame` is a data type (a type for variables!) that can hold structured data. 

In structured data, data are  represented in a rectangular table. Each column is a variable (feature) and each row is an observation (record).
"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

"""## Subset of records (by Index)

you can subset records (rows) by index using `.loc[]`
"""

print(df.loc[0])

print(type(df.loc[0]))

print(df.loc[[0,1]])
print(type(df.loc[[0,1]]))

"""## Subset of variables"""

df['calories']

df.calories

var = "duration"
print(df[var])

"""**subset both records and variables**"""

print(df[["duration","calories"]].loc[1:2])

"""## Importing data"""

Data = pd.read_csv("https://git.nomics.world/dbnomics-source-data/bis-source-data/-/raw/master/BIS_MACRO.csv?inline=false")

# pd.read_xlsx()   # to read excel data
# pd.read_feather() # to read feather binary table format (from Apache arrow)
# pd.read_parquet() # to read parquet binary table format (from Apache arrow)

"""## Subset rows by condition"""

s = Data.columns
s1 = s[s.str.contains("20")]
s2 = s[s.str.contains("_") & s.str.contains("#")]
s3 = s2.append(s1)

DataSub = Data[s3].loc[Data['REF_AREA']=="US"]

years = s1.to_numpy()
USM1 = Data[s1].loc[(Data['REF_AREA']=="US") & (Data['BIS_TOPIC']=="ABBA")].to_numpy()[0]


print(USM1)

import matplotlib.pyplot as plt
plt.plot(years,USM1)
plt.show()

"""## Add variables to `DataFrame` using `assign()`"""

df

df = df.assign(cpd=df.calories/df.duration)

df

"""## Sort """

df = df.sort_values("cpd")

df

# sorting does not change indexes
df.loc[1]

# to renew indexes based on new order:
df = df.reset_index(drop=True)

print(df)

df.loc[1]

"""#Reshaping"""

D3 = Data[s3]
D3

"""## Wide to long: `melt`"""

DM = pd.melt(D3,id_vars=s2,value_vars=s1)
DM

"""# Rename columns using `rename({},axis=)`"""

CPIData = DM.loc[DM['BIS_TOPIC#'].str.contains("Consumer prices, all items, P.C.CH. NSA")]

CPIData = CPIData.rename({"variable":"Year","value":"Inflation"}, axis='columns')

CPIData

"""## Long to wide: `pivot`"""

WD = pd.pivot(CPIData,columns="REF_AREA#",index="Year",values="Inflation")

WD

import matplotlib.pyplot as plt

WD = WD.assign(Year=WD.index)

print(WD.columns)

plt.plot(WD.Year,WD.Canada)
plt.plot(WD.Year,WD.Australia)
plt.plot(WD.Year,WD.Turkey)
plt.plot(WD.Year,WD.Argentina)
plt.plot(WD.Year,WD['Saudi Arabia'])
plt.legend(["Canada","Australia","Turkey","Argentina","Saudi Arabia"])
plt.show()

"""# Plot several series using `seaborn` and long data"""

import seaborn as sns

sns.lineplot(data=CPIData, x='Year', y='Inflation', hue='REF_AREA#')
sns.set(rc={'figure.figsize':(25,13)})

"""# Summerizing (Aggregating)"""

print("all time average: ",
      CPIData['Inflation'].mean())

print("all time average: ",
      CPIData['Inflation'].agg('mean')) 

print("2020 average inflation: ",
      CPIData.Inflation.loc[CPIData.Year=='2020'].mean())

print("2019 average inflation: ",
      CPIData.Inflation.loc[CPIData.Year=='2019'].mean())

"""# Summerizing over groups"""

print("\nAll time averages by countries:")
print(CPIData.groupby(['REF_AREA#'])['Inflation'].mean())

"""# Combining data
## Binding: `append`
"""

data1 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

data2 = {
  "calories": [100, 500, 1000],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

dfm = df1.append(df2, ignore_index=True)
dfm

"""# `merge`"""

data3 = {
  "weight": [100, 500, 1000]
}
df3 = pd.DataFrame(data3)


all = df1.merge(df3,left_index=True,right_index=True)
all