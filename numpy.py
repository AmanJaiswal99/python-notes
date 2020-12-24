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

# mathematical operations on two numpys x and y

# add two numpy
np.add(x,y)

# subtract two numpy
np.subtract(x,y)

# multipy corresponding elements of two numpy 
np.multiply(x,y)

# divide two numpy
np.divide(x,y)

# square root every element of numpy x
np.sqrt(x)

# scalor product or dot product of two numpy of same size
np.dot(x,y)
x.dot(y)

# inner product of two matrix x and y
np.dot(x,y)

# transpose a matrix x
x.T

# sum of all elements of an a numpy x
np.sum(x)

# sum of elements of an array by row
np.sum(x,axis=0)

# sum of elements of an array by column
np.sum(x,axis=1)