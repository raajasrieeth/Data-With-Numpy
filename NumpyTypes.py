# Initialize different arrays in NumPy
import numpy as np

# Generate 0's matrix
z = np.zeros((3, 7))  # generates a 2D array with 3 rows and 7 columns , and all elements as 0s
# print(z)  # Generate evenly spaced values.

more_z = np.zeros((3, 4, 5))
# print(more_z.ndim)    # 3D
# print("More arrays with Zeros:", more_z)

# Ones matrix
o = np.ones((2, 3), dtype='int8')  # Generate an array with all the elements equal to 1.
# print(o)

# Full method
a = np.full((2, 2), 45, dtype='int8')  # Make a 2x2 array with all elements as 45. 2 required arguments: Shape, value.

# Full-like method.
fl = np.full_like(z, 33)  # replicates the shape of the provided array and fills it with provided values.

# Matrix with random decimal numbers
r = np.random.rand(3, 2)  # Generate random values between 0 and 1. The provided arguments are the shape.

# Matrix with Random decimal values, but by providing an already existing shape:
rs = np.random.random_sample(z.shape)  # uses the tuple format to provide its shape and
# generates random values between 0, 1

# Get Random Integer Values:
ri = np.random.randint(0, 4, size=(2, 3) , dtype='int8')   # start , stop  , size(shape of the needed array)
# start defaulted at 0 ; stop not counted ; size defaulted to None(Returns 1 random integer between the limits.)
# print(ri)

# Identity Matrix:
# Square matrix with ones and zeros
im = np.identity(3, dtype='int8')  # only one needed parameter , the 'side of the matrix square'

arr_ls = np.linspace(4, 10, 100)  # return 100 evenly-spaced values between 4 and 10.
# print(arr_ls)