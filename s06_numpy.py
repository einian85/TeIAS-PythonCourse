# -*- coding: utf-8 -*-
"""S06 - numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1edCbvvTIReVihWAJIS_7VP0sOCYI45Wp

## numpy
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

# Why native python lists are not what we want!

a = [1, 2, 3, 5]
b = 4
print(b*a)

import numpy as np

a = np.arange(6)

print(a)

type(a)

b = np.array([1, 2, 3, 4, 5, 6])
print(b)

print(3*b)

print(b * 9 / 5 + 32)

print(a[0])

"""**Arrays of higher dimensions**"""

# more than one dimension
i = np.array(10)
j = np.array([1,2,5,6,8])
k = np.array([[1,2,5,6,8], [4,10,5,9,12]])
l = np.array([[[3,4],[5,6]],[[34,43],[12,11]]])

print(i.ndim)
print(j.ndim)
print(k.ndim)
print(l.ndim)

print(i.size)

"""**Indedxing `numpy` arrays**"""

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[1])

print(a[1,2])

print(a)

np.empty(2)

x = np.arange(0,10,2)
y = np.linspace(0,8,5)

print(x,y)

print(np.linspace(2,3,100,endpoint=False))

np.concatenate((x,y))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print(x)
print(y)

print(np.concatenate((x, y), axis=0))    # rbind
print(np.concatenate((x, y), axis=1))    # cbind

z =array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
print(z)

z.ndim

z.mean()

np.mean(z)

z.shape[1]

for i in range(0,z.shape[0]):
  print(z[i,:,:], "\n**\n**\n")

print(z)