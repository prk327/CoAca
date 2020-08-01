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

'''2D Array
Description
From a 2D array extract all the rows of the 2 column.
Hint: 2 column will have index value as 1.'''
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
import numpy as np
array_2d =np.array(input_list) 

print(array_2d[ : ,1])
