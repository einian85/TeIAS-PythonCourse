# -*- coding: utf-8 -*-
"""S01 - Intro + Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wQpAHpzgyKj-LQQhOuJxrHUMH16j4h8F

# Python Programming for Students of Economics
## Summer 2022

After you learn the basics, it's mostly about googling stuff!
![image.png](https://preview.redd.it/ms8u3bl2kw351.jpg?auto=webp&s=b6540cc2bba22dd7d2961096f31f4368055ce740)

## Programming Languages

* Compiled (C, C++, Fortran, Go, ...)
* Interpreted (Python, R, ...)
* Compiled into intermediate languages (Java, C#, ...)
* JIT Compiled (Julia, ...)

Distributions:

* Compiler / Interpreter
* IDE
* Selected libraries
* Other tools

Languages we will use:

* Python (mostly)
* R
* Julia

Methods to write and run code!

* write code in an editor and save, run in console
* do the above in an IDE (eg. spyder / RStudio)
* get into REPL, write and run there
* use the notebook method (Jupyter)


## Anaconda Python Distribution
Anaconda: https://www.anaconda.com/

Download https://www.anaconda.com/products/individual-d and Install


## Julia
Julia Language: https://julialang.org/

Download https://julialang.org/downloads/ and install

Enable using Julia in Jupyter:

```{Julia}
using Pkg
Pkg.add("IJulia")
```

## R
R Project: https://www.r-project.org/

Download https://cloud.r-project.org/bin/windows/base/ and Install

Enable using R in Jupyter:

```{r}
install.packages("IRkernel")
IRkernel::installspec()
```


# Some comparisons:
[VOX EU: Which programming language is best for economic research: Julia, Matlab, Python or R?](https://voxeu.org/article/which-programming-language-best-economic-research)


[Aruoba, S. B., & Fernández-Villaverde, J. (2015). A comparison of programming languages in macroeconomics. Journal of Economic Dynamics and Control, 58, 265-273.](https://sci-hub.se/10.1016/j.jedc.2015.05.009)

[Open Risk Manual: Overview of the Julia-Python-R Universe](https://www.openriskmanual.org/wiki/Overview_of_the_Julia-Python-R_Universe)

[Julia Language: Noteworthy Differences from other Languages](https://docs.julialang.org/en/v1/manual/noteworthy-differences/)

[QuantEcon Cheatsheets: MATLAB–Python–Julia cheatsheet](https://cheatsheets.quantecon.org/)


Notes on programming (will have more later):

The two main principles for coding and managing data are:

1. Make things easier for your future self
2. Don’t trust your future self

## References
[Numerical Python](https://www.apress.com/gp/book/9781484242452)

![image.png](https://www.haio.ir/app/uploads/2021/12/Numerical-Python.jpg)

[W3Schools Python](https://www.w3schools.com/python/default.asp)

good sources:

* [Jesús Fernández-Villaverde Teachings](https://www.sas.upenn.edu/~jesusfv/teaching.html)
* [QuantEcon](https://quantecon.org/)

## Program as a series of _statements_
"""

print("Hellow world!")
print("This is a python code!")
print("The code for this program might be different in a lot of other languages!")

"""## Assignments 
Think of variable as a kitchen bowl that keeps something in it. name of the variable is the label on the bowl!
Assignment is to pour stuff in a bowl (maybe from other bowls)!
![image.png](https://www.wmfnordic.com/assets/image-cache/images/media/A12D437B-A7BA-43B0-9813579AE1721002.a83d4af7.jpg)
"""

a = 1
b = 2

print(a)

a = a + 1
print(a)

# we use # sign for comments
# it means the rest of the line will not run
# b = 3
print(b) # you can use it after a sentence too!

"""**naming rules** (specific to python, each language has it's own rules):
* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
* Variable names are case-sensitive (`age`, `Age` and `AGE` are three different variables)
"""

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

# Naming Conventions
variable_name = 3
VaribaleName = 5
variableName = 4

Student_ID = 4
StudentID = 86205022

print(Student_ID)