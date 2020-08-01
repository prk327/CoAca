'''Vectorize Numpy
Description
Given an array, 'array_3' divide each element with 5. 
Hint: Create a vectorized function, then apply it to the array_3.'''

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_1 = input_list[0:2]
list_2 = input_list[2:4]
import numpy as np
array_1 = np.array(list_1)
array_2 = np.array(list_2)
array_3 =np.hstack((array_1,array_2))

#non np way
#function = [x/5 for x in array_3]
function = np.vectorize(lambda x: x/5)  

print(function(array_3))
