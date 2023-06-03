## remember to pip install numpy first

## Numpy requires less bytes of memory that's why it's faster than list
## Numpy is Matlab replacement

## Load Numpy
import numpy as np

## Initialize an array
x = np.array([[10,20,30],[4.0,5.0,6.0]], dtype="int8")
print(x)

## Get dimensions of an array
print(x.ndim)
## Get shape
print(x.shape)
## GEt data type
print(x.dtype)
## Get size in bytes
print(x.itemsize)
## Get number of elements
print(x.size)

