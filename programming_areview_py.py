# -*- coding: utf-8 -*-
"""Programming-AReview-Py.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HEKw_FL9HX_xTUv2qDHrQrXv-chGuIgX

# Programming Course:  A Review

## (Python Version)

## Concepts we want to learn
* Program as a series of _statements_
* Assignment 
* Data Types
* Operators (including Logical Operators)
* Program Flow Control: Conditions
* Keeping more than one value: `list`s, `tuple`s, `set`s, `dict`iornaries
* Program Flow Control: Loops
* Program Flow Control: Functions
* Using Other peoples' code: modules, packages, libraries, and frameworks
* Intro to numpy and scipy
* numpy arrays
* random numbers
* Intro to matplotlib
* A lot of use cases and examples

After you learn the basics, it's mostly about googling stuff!
![image.png](attachment:6e8d75d2-6b09-4d0d-a4db-e3f827f40b58.png)

## Programming Languages

* Compiled
* Interpreted
* JIT Compiled

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
![image.png](attachment:6249fd7f-a35f-4041-a400-c18f4fa86bb8.png)

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

"""## Data Types

**Primary types**

* Text type:  `str`
* Numeric Types: `int`, `float`, `complex`
* Boolean Type: `bool`

**Types for more than one value**

* Sequence Types: `list`, `tuple`, `ranage`
* Mapping Type: `dict`
* Set Types: `set`, `frozenset`

"""

x = 12
print(type(x))

# you can change the type of a variable in python by assigning a value of new type!
x = "Hi"
print(type(x))
# not all langugages are like this!

x = 33.45
print(type(x))

x = True # or False
print(type(x))

# Working with numbers
x = 17.2
y = int(x)
print(y)
print(type(y))

z = float(y)
print(z)
print(type(z))

# you can use int and float to change from str too!
# very useful when you read some number from input or a file!
input_from_user = input()
print(input_from_user)
print(type(input_from_user))

n = int(input_from_user)
print(n)
print(type(n))

# using scientific notation
pop = 8.3e7 # population of Iran!
print(pop)

# we can use both 'single quates' and "double quates" for string
str1 = "Hello"
str2 = 'Hi'

# three double/single quates for multiline string
Text = """لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.
چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط
فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد. کتابهای زیادی در شصت
و سه درصد گذشته، حال و آینده شناخت فراوان جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری
را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد. در این صورت 
می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها و شرایط سخت تایپ به پایان رسد وزمان مورد نیاز
شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد."""

print(Text)

# use `len` to get the number of characters in a string
print(len(Text))

"""## Operators
**Arithmatic Operators**
* Addition: `+`
* Subtraction: `-`
* Multiplication: `*`
* Division: `/`
* Integer division: `//`
* Integer division modulus: `%`
* Exponentiation: `**`
"""

print(3 + 5)
print(3 - 5)
print(3 * 5)
print(5 / 3)
print(5 // 3)
print(5 % 3)
print(5 ** 3)

"""**Assignment Operators**
* `+=`
* `-=`
* `*=`
* `/=`
* ...
"""

x = 5
x += 3
print(x)

"""**Comparison Operators**
* Equal: `==`
* Not equal: `!=`
* Greater than: `>`
* Less than: `<`
* Greater that or equal to: `>=`
* Less than or equal to: `<=`
"""

print(8<5)

comp = 8 < 5
print(type(comp))

"""**Logical Operators**
* `and`
* `or`
* `not`
"""

print(x > 5 and x <10)

"""**Identity Operators**
* `is`
* `is not`
"""

x = 3
y = int(3)
print(x is y)

"""**Membership Operators**
(for strings and for sequence types)
* `in`
* `not in`
"""

print("e" in "Majid!")

"""**Bitwise Operators** (Advanced)
* `&` (bitwise AND)
* `|` (bitwise OR)
* `^` (bitwise XOR)
* `~` (bitwise NOT)
* `<<` (bitwise left shift)
* `>>` (bitwise right shift)
"""

# this shifts all bits of 4, one bit to the left
# that is 000100 becomes 001000
print(4 << 1)

"""## Program Flow Control: Conditions
You don't always want the statements to be evaluated line by line and in order.

Sometimes you want to run an statement only if a condition holds.

**`if`**
"""

a = 30
b = 100
if b > a:
    print("b is greater than a!")

# It is important to use indentation to specify the part of code that is run conditional on the condition.
a = 30
b = 3
if b > a:
    print("b is larger")
print("than a!") #this is out of if block, because it is not indented!

"""**`else`**"""

a = 13
b = 10
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b or equal to b")

"""**`elif`**"""

a = 13
b = 10
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

"""**short versions**:"""

# one line `if`
if a > b: print("a is greater than b")
    
# one line if else
print("A") if a > b else print("B")

"""**Logical Operators in Conditions**"""

a = 100
b = 50
c = 200

if c>a and c>b:
    print("c larger than both a and b")

"""**Nested `if`**"""

x = 19

if x > 10:
    print("Above Ten: Pass!")
    if x > 17:
        print("and above 17: A!")
    else:
        print("but not A!")

"""## Keeping more than one value: `list`s, `tuple`s, `set`s, `dict`iornaries

|         | `list` | `tuple` | `set` | `dict` |
|---------|--------|---------|-------|--------|
| mutable |  ✔    |   ❌    |  ✔    |     ✔ |
| duplicate values |  ✔ | ✔ |❌ |❌(key)/✔(value)|
| ordered | ✔ | ✔ | ❌ |❌ |
| how to build | `[a,b,a,d]` | `(a,b,a,d)` | `{a,b,c,d}` | `{a:b,c:d}` |
| how to build| `list()` | `tuple()` | `set()` | `dict()` |
| indexing | `[i]` | `[i]` | ❌ |  `[key]` |
| add new value | `.append(v)` | ❌ | `.add(v)` | `.update({k:v})` | 
| remove item | `.pop(i)` | ❌ | `.pop(i)` | `.pop(k)` |
| sort | `.sort()` | ❌ | ❌ |  ❌ (you can do some stuff utilizing`sorted()` |
| find first element | `.index(v)` | `.index(v)` | ❌ | `.get(k)` |
| count all found elements | `.count(v)` | `.count(v)` | ❌ | ❌ |
| reverse | `.reverse()` |  ❌ | ❌ | ❌ |
 
"""

my_list = [1,8,7,12,13,11,8]
my_tuple = (1,8,7,12,13,11,8)
my_set = {1,8,7,12,13,11,8}
my_dict = {'a':1,'c':8,'e':7,'d':12,'b':13,'f':11,'g':8}

print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)

new_list_from_tuple = list(my_tuple)
print(new_list_from_tuple)

new_set_from_tuple = set(my_tuple)
print(new_set_from_tuple)

new_set_from_list = set(my_list)
print(new_set_from_list)

new_list_from_set = list(my_set)
print(new_list_from_set)

new_dict = dict({'a':1,'b':8,'c':7,'d':12,'e':13,'f':11,'g':8})

# indexing

print(my_list[3])    # item 3 (4th item as index starts from 0)
print(my_list[2:4])  # items 2 up to (not including) 4
print(my_list[:4])   # from start up to (not including) item 4
print(my_list[2:])   # from item 2 to the end

print(my_tuple[2:4])

print(my_set[2])   # No indexing for sets!

print(8 in my_set)

print(my_dict['d'])

my_list.append(5)
print(my_list)

my_set.add(5)
print(my_set)

my_dict.update({'h':12})
print(my_dict)

a = my_list.pop(3)
print(my_list)

print(a)

my_set.pop()
print(my_set)

v = my_dict.pop("d")
print(my_dict)
print(v)

my_list.sort()
print(my_list)

idx = my_list.index(8)
print(idx)

idx = my_tuple.index(8)
print(idx)

v = my_dict.get("e")
print(v)

n = my_list.count(8)
print(n)

n = my_tuple.count(8)
print(n)

my_list.reverse()
print(my_list)

"""**`range`**"""

# range(start,end,step)  
# end is not included itself
my_range = range(0,10,2)
print(my_range)

list_from_range = list(my_range)
print(list_from_range)

# `range` can only have integer steps
new_range = range(0,10,.5)
# to create sth like that, you will need `arange` from `numpy`

"""# Program Flow Control: Loops
`for` loop for a know number of iterations. A `for` loop is used for iterating over a sequence (that is either a `list`, a `tuple`, a `dict`ionary, a `set`, or a `str`ing).

`while` for unknown number of iterations (conditional)
"""

fruits = ["apple","banana","cherry"]
for f in fruits:
    print(f)

# Print all numbers from 0 to 10 (not 10 itself)
for i in range(0,10):
    print(i)

# count all 2-digit odd numbers 
n = 0
for i in range(10,100):
    if i % 2 == 1:
        n += 1
print(n)

# You can loop through characters of a string!
for c in "Hello World!":
    print(c)

"""**`break`**"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

"""**`continute`**"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

"""**`else`** in `for` loop"""

for i in range(2,6):
    print(i)
else:
    print("done")

for i in range(1,20):
    if i==10 :
        break
    print(i)
else:
    print("done")

for i in range(1,20):
    if i==10 :
        continue
    print(i)
else:
    print("done")

"""**nested loops**"""

for n in range(0,10):
    for x in range(0,10):
        print("*",end='')
    print("")

for n in range(0,10):
    for x in range(n, 10):
        print("*",end='')    #note the end parameter of print
    print("")

"""**`while`** loop"""

j = int(input())
s = ""
while j>0:
    d = j % 2
    s = str(d) +s
    j = j // 2
print(s)

"""`else`, `break` and `continue` work for `while` loops too.

0
1
10 = 2
11 = 3
100 = 4
110 = 6
1000000 = 64 
11111111 = 255

## Functions
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
"""

def my_function():
    print("Hello from a function")

"""as you can see, the above code dose *not* print anything, as it is not yet *called*."""

my_function()  # name of the function + () to call it

"""**Arguments** (args/Parameters)
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
"""

def say_hi(name):
    print("Hi "+name,"!")

say_hi("Ali")
say_hi("Saeed")
say_hi("Zahra")

say_hi()

def say_hello(fname, lname):
    print("Hello "+fname + " " + lname+"!")

say_hello("Majid", "Einian")

say_hello("Jacob")

"""If the number of arguments is unknown, add a * before the parameter name. 

You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

for more info see https://www.w3schools.com/python/python_functions.asp

**Return Values**
To let a function return a value, use the `return` statement:
"""

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

"""**Recursive Functions**"""

def fct(i):
    if i==0:
        return 1
    else:
        return i*fct(i-1)

fct(10)

"""## Using Other peoples' code: modules, packages, libraries, and frameworks

**Module** is a file which contains various Python functions and global variables. It is simply just .py extension file which has python executable code.

**Package** is a collection of modules. It must contain an init.py file as a flag so that the python interpreter processes it as such. The init.py could be an empty file without causing issues.

**Library** is a collection of packages.

**Framework** is a collection of libraries. This is the architecture of the program.
"""

import math

print(math.sin(math.pi/6))

import math as m

print(m.sin(m.pi/6))

from math import sin, pi

print(sin(pi/6))

from math import sin, pi

print(sin(pi/6))
print(cos(pi/6))

from math import * # not recommended 

print(sin(pi/6))
print(cos(pi/6))

"""**Methods**

| Method | Description |
|--------|-------------|
| `acos()`| arc cosine |
| `acosh()`| inverse hyperbolic cosine |
| `asin()`| arc sine |
| `asinh()`| inverse hyperbolic sine |
| `atan()`| arc tangent |
| `atan2()`| arc tangent of y/x |
| `atanh()`| inverse hyperbolic tangent |
| `ceil()`| Rounds a number up to the nearest integer |
| `comb()`| number of ways to choose k items from n items without repetition and order |
| `copysign()`| Returns a float consisting of the value of the first parameter and the sign of the second parameter |
| `cos()`| cosine |
| `cosh()`| hyperbolic cosine |
| `degrees()` | Converts an angle from radians to degrees |
| `dist()` | Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point |
| `exp()` | Returns E raised to the power of x | 
| `expm1()` | `exp()-1` |
|`fabs()` |   absolute value of a number| 
 |`factorial()` | the factorial of a number| 
 |`floor()` | Rounds a number down to the nearest integer| 
 |`fmod()` |  remainder of x/y| 
 |`frexp()` | Returns the mantissa and the exponent, of a specified number| 
 |`fsum()` |  sum of all items in any iterable (tuples, arrays, lists, etc.)| 
 |`gamma()` |  gamma function at x| 
 |`gcd()` |  greatest common divisor of two integers| 
 |`hypot()` |  Euclidean norm| 
 |`isclose()` | Checks whether two values are close to each other, or not| 
 |`isfinite()` | Checks whether a number is finite or not| 
 |`isinf()` | Checks whether a number is infinite or not| 
 |`isnan()` | Checks whether a value is NaN (not a number) or not| 
 |`isqrt()` | Rounds a square root number downwards to the nearest integer| 
 |`ldexp()` |  inverse of `frexp()` which is `x * (2**i)` of the given numbers x and i| 
 |`lgamma()` |  log gamma value of x| 
 |`log()` |   natural logarithm of a number, or the logarithm of number to base| 
 |`log10()` |   base-10 logarithm of x| 
 |`log1p()` |   natural logarithm of 1+x| 
 |`log2()` |   base-2 logarithm of x| 
 |`perm()` |   number of ways to choose k items from n items with order and without repetition| 
 |`pow() `|   value of x to the power of y| 
 |`prod()`|   product of all the elements in an iterable| 
 |`radians() `| Converts a degree value into radians| 
 |`remainder()`|   closest value that can make numerator completely divisible by the denominator| 
 |`sin()` |   sine of a number| 
 |`sinh()` |   hyperbolic sine of a number| 
 |`sqrt()` |   square root of a number| 
 |`tan()` |   tangent of a number| 
 |`tanh()` |   hyperbolic tangent of a number| 
 |`trunc()` |   truncated integer parts of a number |

**Constants**
 
| Constant | Description |
|----------|-------------|
| `e` | Euler's number (2.7182...) |
| `inf` | floating-point positive infinity |
| `nan` |floating-point NaN (Not a Number) value |
| `pi` | $\pi$ (3.1415...) |
| `tau` | $\pi \times 2$ |
"""

sin(radians(30))

print(floor(3.13))
print(ceil(3.13))

print(floor(-3.3))
print(ceil(-3.3))

print(int(3.13))
print(int(-3.3))

print(trunc(3.13))
print(trunc(-3.3))

print(trunc(-3.8))
print(int(-3.8))
print(ceil(-3.8))
print(floor(-3.8))

"""## numpy
NumPy (pronounced /ˈnʌmpaɪ/ (NUM-py) or sometimes /ˈnʌmpi/ (NUM-pee)) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

## scipy
SciPy (pronounced /ˈsaɪpaɪ/ "sigh pie") is a free and open-source Python library used for scientific computing and technical computing.

* `cluster`: hierarchical clustering, vector quantization, K-means
* `constants`: physical constants and conversion factors
* `fft`: Discrete Fourier Transform algorithms
* `fftpack`: Legacy interface for Discrete Fourier Transforms
* `integrate`: numerical integration routines
interpolate: interpolation tools
* `io`: data input and output
* `linalg`: linear algebra routines
* `misc`: miscellaneous utilities (e.g. example images)
* `ndimage`: various functions for multi-dimensional image processing
* `ODR`: orthogonal distance regression classes and algorithms
* `optimize`: optimization algorithms including linear programming
* `signal`: signal processing tools
* `sparse`: sparse matrices and related algorithms
* `spatial`: algorithms for spatial structures such as k-d trees, nearest neighbors, Convex hulls, etc.
* `special`: special functions
* `stats`: statistical functions
"""

import numpy as np
import scipy.stats as st

a = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
print(a)

b = np.array(a)
print(b)
print(type(b))

print(b * 9 / 5 + 32)

# you cannot do this kind of calculation with python lists
print(a * 9 / 5 + 32)

print(a[3])

print(b[3])

i = np.array(10)
j = np.array([1,2,5,6,8])
k = np.array([[1,2,5,6,8], [4,10,5,9,12]])
l = np.array([[[3,4],[5,6]],[[34,43],[12,11]]])

k = np.array([[1,2,5,6,8], [4,10,5,9,12]])

print(i.ndim)
print(j.ndim)
print(k.ndim)
print(l.ndim)

"""# Indedxing `numpy` arrays"""

print(j[2])

print(k[1,4])

print(l[1,0,0])

print(l[0,1,0])

print(i)

k[0,0,0]

"""**negative indexing**"""

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

a = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])

print(a[1:7:2])

print(a[::2])

print(a[1::2])

"""**slicing in multi-dimentional arrays**"""

