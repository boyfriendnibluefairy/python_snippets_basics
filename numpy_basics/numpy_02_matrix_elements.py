import numpy as np

sample_array = np.array([
    [14, 15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30, 31]
])
#print(sample_array.shape)

## Get specific element [r,c], index starts at 0
print(sample_array[2,4])

## Get specific row
print(sample_array[0,:])

## Get specific column
print(sample_array[:,2])

## Get small portion of matrix [start_index, end_index, step_size]
print(sample_array[2, 0:5:2])