'''Checkerboard Matrix
Description
Given an even integer ‘n’, create an ‘n*n’ checkerboard matrix with the values 0 and 1, using the tile function.
 
Format:
Input: A single even integer 'n'.
Output: An 'n*n' NumPy array in checkerboard format.

Example:
Input 1:
2
Output 1:
[[0 1]
 [1 0]]
Input 2:
4
Output 2:
[[0 1 0 1] 
 [1 0 1 0]
 [0 1 0 1]
 [1 0 1 0]]'''
 
 # For a video solution of the code, copy-paste the following link in your browser:
# https://youtu.be/cak6Y6yN4AU

# Read the variable from STDIN
n = int(input())

import numpy as np

# Create the smallest unit of a checkerboard matrix
x = np.array([[0, 1], [1, 0]])

# Create a checkerboard matrix of size n*n using the tile() function. We use n//2 
# since the smallest unit of a checkerboard matrix is already of size 2*2. So, for 
# creating a larger matrix, say, of size 8, we need to replicate it using the tile()
# function 4 times as it will then give a matrix of size 8*8.
check = np.tile(x, (n//2, n//2))

# Print the created matrix
print(check)
