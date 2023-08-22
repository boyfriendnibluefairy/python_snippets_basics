import tensorflow as tf

## Create a tensor with n elements, for example,
## we can use tf.range() function to create tensor
## with n = 36 elements
#X = tf.range(36)
#my_dataset = tf.data.Dataset.from_tensor_slices(X)
#print(my_dataset)
#print("==========")
## from_tensor_slices() chops the elements into
## separate tensor objects
#for item in my_dataset:
#    print(item)

## How to chain transformations
X = tf.range(6)
my_dataset = tf.data.Dataset.from_tensor_slices(X)
# my_dataset = my_dataset.repeat(2)
# for item in my_dataset:
#     print(item)
# my_dataset = my_dataset.repeat(2).batch(2)
# for item in my_dataset:
#     print(item)

## Since dataset methods do not modify the original dataset,
## you have to use the map() function to apply preprocessing
## and then save the result to a new variable:
# doubled_values = my_dataset.map(lambda x: x*2)
# for item in doubled_values:
#     print(item)

## filter() function works like a regular filter
## that access data depending on the condition:
# values_greater_than_three = my_dataset.filter(lambda x: tf.reduce_sum(x) > 3)
# for item in values_greater_than_three:
#     print(item)

## take() function takes n items from your tensor
# for item in my_dataset.take(3):
#     print(item)

## How to shuffle a subset of your dataset
my_dataset = tf.data.Dataset.range(16)
# for item in my_dataset:
#      print(item)
shuffled = my_dataset.shuffle(buffer_size=6, seed=42).batch(3)
for item in shuffled:
     print(item)