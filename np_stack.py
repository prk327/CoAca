'''Stack Three Arrays
Description
Horizontally stack two arrays using hstack, and finally, vertically stack the resultant array with the third array.

Example:
Input 1:
[[1, 2],
 [5, 6]]

[[3, 4],
 [7, 8]]

[[9, 10, 11, 12]]
Output 1:
[[1 2 3 4]
 [5 6 7 8]
 [9 10 11 12]]
'''

# Read the input
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_1 = input_list[0]
list_2 = input_list[1]
list_3 = input_list[2]

# Import NumPy
import numpy as np

# Write your code here
# Write your code here
a = np.array(list_1).reshape(2,2)
b = np.array(list_2).reshape(2,2)
c = np.array(list_3).reshape(1,4)

d = np.hstack((a,b))

print(np.vstack((d,c)))
