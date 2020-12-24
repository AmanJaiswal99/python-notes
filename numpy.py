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

#make an array of 0 as items with a certain shape
arr = np.zeros((m,n))

# make an array of 0 as items of dimension 2x3 with a datatype of string
arr = np.zeros((2,3),dtype=string)

# make an array of 1 as items with a certain shape
arr = np.ones((m,n,k))

# range function
arr = np.arrange(initial,final,step)

# create an array with n number of items within a certain range
arr = np.linspace(start,stop,n)

# create an array with a fixed dimension populated with a number k
arr = np.full((m,n),k)

# create an identity matrix

arr = np.eye(m)

# create an array with random numbers

arr = np.random.random((m,n))