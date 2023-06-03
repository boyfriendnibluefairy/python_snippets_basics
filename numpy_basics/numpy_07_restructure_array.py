import numpy as np

old_array = np.array([[1,2,3],[4,5,6]])
#print(old_array)
## Reshaping requires preserving the same number of elements
reshaped_array = old_array.reshape((1,6))
#print(reshaped_array)

## Vertical Stacking of Arrays
r1 = np.array([1,2,3])
r2 = np.array([4,5,6])
#print(np.vstack([r1,r2,r2,r2]))

## Horizontal Stacking of Arrays
c1 = np.zeros((2,3))
c2 = np.ones((2,3))
print(np.hstack([c1,c2]))