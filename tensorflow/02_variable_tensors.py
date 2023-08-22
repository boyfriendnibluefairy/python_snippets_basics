## When we need to change the element values of
## a tensor over time, e.g. weights of neural
## networks, we need to create tensor using
## tf.Variable(). However, in machine learning,
## you will rarely create your own tf variables
## because Keras already do it for you under the hood.
import tensorflow as tf

# t = tf.constant([
#     [1., 0., 1.],
#     [3., 6., 9.]
# ])
# print(t)
# print("=========")
v = tf.Variable([
    [1., 2.],
    [3., 4.],
    [5., 6.]
])
# print(v)

## element-wise operation
# print(v)
# print("=========")
# v.assign(v + 3)
# print(v)

## replace an element value
# print(v)
# print("=========")
# v[1,1].assign(100)
# print(v)

## how to use tf.where() function
## first case:  tf.where(condition)
## second case: tf.where(condition, x, y)

## first case example:
#print(tf.where([True, False, False, True]))

## second case example:
# print(tf.where([True, False, False, True], [1,2,3,4], [10]))

## verdict: When the only argument is condition, it returns the index
## of true values. When argument inludes (condition, x, y), where()
## function replaces true values with the corresponding x[] values
## and false values with the corresponding y values