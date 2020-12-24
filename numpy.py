# import numpy package
import numpy as np 

# create a simple array

arr = np.array([1,2,3])

# check shape

arr.shape

# check dimensions

arr.ndim

# check size i.e number of elements

arr.size

# accessing elements from multidimensional arrays

arr[m,n]

# appending to an array

arr = np.append(arr[position],element to be inserted)

# deleting element from an array

arr = np.delete(arr,position)
arr = np.delete(arr[m],n)