'''2D Array
Description
Create an array using list list_1 = [10,11,12,13] and list_2 = [15,12,13,14] and print the shape and dimension of the array created.'''

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_1 = input_list[0]
list_2 = input_list[1]

import numpy as np
array_1 = np.array([list_1,list_2])

print(array_1.shape)
print(array_1.ndim)
