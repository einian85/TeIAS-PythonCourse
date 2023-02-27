# -*- coding: utf-8 -*-
"""S07 - numpy + plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pOQQnJV-bUbK0LIk1fo-2XYyx6aWfaKu

**negative indexing**
"""

import numpy as np
j = np.array([1,2,5,6,8])

print(j)
print(j[-2])
print(j[-1])

"""**parts of array**"""

print(j[2:4])

print(j[2:])
print(j[:2])

print(j[-3:-1])

print(j[-3:])

print(j[len(j)-1])

print(j[-1])

print(j[len(j)])

a = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])

print(a[1:7:2])

print(a[::2])

print(a[1::2])



"""**Internal types of numpy**"""

l = [1, 2, 3, "H"]
a = np.array([1,2,3,"H"])

print(l)
print(a)

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i8')

print(arr)
print(arr.dtype)

arr = np.array([1,2,3,4],dtype=float)
print(arr)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
arr[0] = 42

print(arr)
print(x)
print(y)

x[0]=100
print(x)
print(arr)

y[0]=200
print(y)
print(arr)

"""##Check if Array Owns it's Data
As mentioned above, copies *own* the data, and views _do not own_ the data, but how can we check this?

Every NumPy array has the attribute `base` that returns `None` if the array owns the data.

Otherwise, the `base`  attribute refers to the original object.
"""

print(x.base)
print(y.base)
print(arr.base)

z=arr

z[0]=300
print(z)
print(arr)

print(z.base)
print(arr.base)

l0 = [1, 3, 5, 7]
l1 = l0.copy()
l1[0]=10
print(l1)
print(l0)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

"""**reshape**"""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.shape)
newarr = arr.reshape(4, 3)

print(newarr)
print(newarr.shape)

#newarr2 = arr.reshape((4,3),order="C")
#print(newarr2)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

newarr = arr.reshape(3, 3)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reshaped = arr.reshape(2, 4)
print(reshaped)
print(reshaped.base)

arr[0] = 100
print(reshaped)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reshaped = arr.reshape(2, 4).copy()
print(reshaped)
print(reshaped.base)

arr[0] = 100
print(reshaped)

"""## Stacking Arrays"""

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

print(np.concatenate((arr1, arr2), axis=1))
print("\n")
print(np.stack((arr1, arr2), axis=1))
print("\n")

print(np.hstack((arr1, arr2)))
print("\n")
print(np.vstack((arr1, arr2)))
print("\n")
print(np.dstack((arr1, arr2)))

x = np.dstack((arr1, arr2))
print(x.shape)

from numpy import random

k = random.randint(10)

print(k)

x = random.rand(5)

print(x)

print(random.rand())

k = random.randint(100, size=10)
print(k)

k = random.randint(100, size=(3,5))
print(k)

x = random.rand(3,5)
print(x)

m = random.choice([3, 5, 7, 9])

print(m)

m = random.choice([3, 5, 7, 9], size=(3, 5))
print(m)

n = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(n)

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

arr = np.array([1, 2, 3, 4, 5])
b = random.permutation(arr)
print(arr)
print(b)
arr[0]=100
print(arr)
print(b)

"""# `matplotlib`"""

import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x = random.normal(size=1000,loc=2)

sns.histplot(x)
plt.show()

"""`rand`
`randint`
`choice`
`normal`

"""

random.standard_normal(100)

from scipy.stats import  norm
x = norm.rvs(2,1,1000)
sns.histplot(x)
plt.show()

sns.kdeplot(random.normal(size=1000))
plt.show()

from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)
print(type(myroot))

print(myroot.x)

import math
my_x = np.arange(-math.pi,math.pi,.01)
my_y = my_x + np.cos(my_x)
plt.plot(my_x,my_y)
plt.plot(my_x,np.repeat(0,len(my_x)))
plt.plot(np.repeat(myroot.x,3),range(-1,2))
plt.show()

print(myroot)

from scipy.optimize import root
from math import cos

def eqn(x):
  return 1.1 + cos(x)

myroot = root(eqn, 0)
print(myroot)