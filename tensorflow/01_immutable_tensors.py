## This python code contains collection of basic commands
## for manipulating tensors in tensor flow.
## Note that tensorflow operations work well with numpy
## and vice versa.
import tensorflow as tf
import numpy as np

## How to create tensors with 3 rows and 4 columns
## Note: tensors created using tf.constant() are immutable
# t = tf.constant([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])

## How to check the shape of the tensor
#print(t.shape)

## How to check the data type of a tensor
#print(t.dtype)

## How to slice tensors
#print(t[:,1:3])

## Python ellipsis are used to concisely access all the elements
## and choose only specific instance. The last array in the print
## function means choose only the first instance. It's equivalent
## to this expression: [:,:, 1] = [..., 1]
## recall that tensorflow thinks in terms of column vectors
# print(t)
# print("======")
# print(t[...,1])

## np.newaxis is used when you want to add an additional
## dimension to the array
# print(t.shape)
# print("======")
# t2 = t[..., tf.newaxis]
# print(t2.shape)

## element-wise addition
# print(t)
# print(t + 100)

## element-wise exponentiation
# print(t)
# print("=========")
# print(tf.square(t))

## matrix multiplication using @
# print(t)
# print("=========")
# print(t @ tf.transpose(t))

## how to save only a scalar value to a tensor variable
# t_scalar = t
# print(t_scalar)
# print("=========")
# t_scalar = tf.constant(36)
# print(t_scalar)

## other basic math operations
# tf.add()
# tf.multiply()
# tf.square()
# tf.exp()
# tf.sqrt()

## numpy similar operations
## *reduce_* means there might be a reduction in precision
## especially when the available GPU is 32-bit
# tf.reshape()
# tf.squeeze()
# tf.tile()
# tf.math.log()
# tf.reduce_mean()
# tf.reduce_sum()
# tf.reduce_max()

## convert np array to tensor and vice versa
# np_array = np.array([1.,2.,3.])
# print(np_array)
# print("=========")
# t = tf.constant(np_array)
# print(t)
# print("=========")
# t = np.array(t)
# print(t)

## tensorflow do not allow type conversion by default
## but you may use tf.cast() if you really need type casting
# t1 = tf.constant(6)
# t2 = tf.constant(6.)
# t3 = t1 + t2 ## expect an exception/error here

