import numpy as np

## all elements are zero
a = np.zeros((5,6), dtype='int8')
#print(a)

## all elements are ones
b = np.ones((2,3), dtype="float16")
#print(b)

## np.full( <shape>, <default value> )
c = np.full(b.shape, 33)
#print(c)

## matrix of random decimal numbers
d = np.random.rand(2,3)
#print(d)

## matrix of random integers (start, end, shape)
e = np.random.randint(-1, 10, size=(3,3))
print(e)