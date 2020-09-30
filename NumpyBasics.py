# I ve added the reference docs.
import numpy as np  # not built in . Needs to be pip installed

'''What is numpy:
It is a multidimensional array library.

Why NumPy over Lists? : Numpy provides a much faster and simpler way to deal with data.
 NumPy is faster because it uses fixed types such as int8 , int16 etc to specify an integer.
 Lists , cycle through 4 steps to get the data into and out of them ie , they need upto 3*64 bits and 1*32 bits to just
 deal with an integer.
NumPy uses lesser memory than lists to contain the same data.
NumPy uses Contiguous Memory. , no free blocks between the memory slots.

Applications of NumPy: 
1--> Math 
2-->Plotting with Matplotlib
3-->Backends
4-->Tensors in machine learning 
5-->And a lot with data!

'''
a = np.array([1, 2, 3],
             dtype='int8')  # type of data, int8 uses 8 bits to specify an integer. , initialize an array  , with a list of parameters.
# specifying data type is useful
# print matrix
b = np.array([[1, 2, 3], [23, 45, 78]], dtype='int16')  # 2D array
print(a, type(a))
print(b, type(b), "Dimension of b is:", b.ndim)
# get dimension
print("Dimension:", a.ndim)
# get shape
print(a.shape)

# get data type:
print(a.dtype)

# get size:
print(a.size)

# get item size:
print(a.itemsize)

# get total size :
print("Bytes in array a: ", a.nbytes)

# changing datasets:
# Create a 2D array:
arr = np.array([[1, 2, 3, 4, 5, 6, 7, ], [8, 9, 10, 11, 12, 13, 14, ]], np.int32)
# Array looks like this;
# [[ 1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14]]

# get specific element
# Syntax: <array_name>[r][c] or <array_name>[r , c]

print(arr[1][2])  # get third element in the second array
# or
print(arr[1, 2])  # does the same thing

# get an entire row:
print(arr[1][:])    # gets the 2nd row , and all columns contained by it
# Syntax to get a row n:
# <array_name>[n][:]
# get an entire column:
print(arr[:,2]) # get the 2nd column
# Syntax to get a column n:
# <array_name>[: , n]

# Custom:
print(arr[0 , 0:5:2])   # get the elements in the first row and skip every other element

# Change an element:
# Syntax: <array_name>[r][c] = <new_value>
print("Initial value:",  arr[0 , 4])
arr[0][4] = 34      # or arr[0 , 4] = 34
print("new value at row 0 and column 4:" , arr[0][4])

# change a row:
arr[0][:] = 1   # make all the elements in the fist row 1 !
print(arr)

# change a column :
arr[: , 2] = 56 # make the second column 56

print(arr)
print(list(i for i in range( 40 , 50)))

# 3D array:
x = np.array([[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ,
               [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
               [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
               ]])
print(x.shape)  # 1 , 3 , 10

# get specific element:
print(x[0][2][5])   # print the 5th element of the third array in the 1st main array  ,
# work from outside to in while dealing with multidimensional arrays.
# iterate over the elements in a NumPy array.
# the number of for loops needed = number of dimensions in the array.
for i in x:
    for element in i:
        for a in element:
            print(a)

# replace a dimension , ie, multi-value replacing

x[: , 0 ,: ] = list(i for i in range(10))
print(x)
print(x[0 , : , :])