import numpy as np

a = np.array((14,15,16,17,18,19))
b = np.array((0,1,0,1,0,1))
#print(a+5)
#print(a*2)
#print(a/5)
#print(a**2)
#print(a+b)

## Take sine value of an array
c = np.sin(a)
#print(c)

### LINEAR ALGEBRA
## In Linear Algebra, we're not doing elementwise computation
a = np.full((3,2), 3)
b = np.ones((2,3))
#print(a)
#print(b)
print(np.matmul(a,b))

## Find the determinant
d = np.identity(6)
print(np.linalg.det(d))