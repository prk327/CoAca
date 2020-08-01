'''Factorial
Description
Given a number ‘n’, output its factorial using reduce().
Note: Make sure you handle the edge case of zero. As you know, 0! = 1

P.S.: Finding the factorial without using the reduce() function might lead to deduction of marks.

Examples:
Input 1:
1
Output 1:
1

Input 2:
3
Output 2:
6 '''

# Import the reduce() function
from functools import reduce

# Write your code here
def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x,y: x*y, range(1,n+1))
