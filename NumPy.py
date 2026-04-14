import numpy as np
a=np.array(42)
print(a)
print(a.ndim)
print()
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.ndim)
print()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
print(arr.dtype)
print(arr.ndim)
print()
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr.ndim)
print()
print(np.__version__)
print()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

print()
# joining array
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
print()
a=np.array([1,2,3])
b=np.array([4,5,6])
arr=np.stack((a,b),axis=1)
print(arr)
print()
arr = np.stack((arr1, arr2), axis=1)

print(arr)
print()
arr = np.hstack((arr1, arr2))

print(arr)
print()
arr = np.vstack((arr1, arr2))

print(arr)
print()
arr = np.dstack((arr1, arr2))

print(arr)
print()
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()