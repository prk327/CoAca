''' Set Operations
Description
In a school, there are total 20 students numbered from 1 to 20. You’re given three lists named ‘C’, ‘F’, and ‘H’, representing students who play cricket, football, and hockey, respectively. Based on this information, find out and print the following: 
Students who play all the three sports
Students who play both cricket and football but don’t play hockey
Students who play exactly two of the sports
Students who don’t play any of the three sports
Format:
Input:
3 lists containing numbers (ranging from 1 to 20) representing students who play cricket, football and hockey respectively.
Output:
4 different lists containing the students according to the constraints provided in the questions.

Note: Make sure you sort the final lists (in an ascending order) that you get before printing them; otherwise your answer might not match the test-cases.

Examples:
Input 1:
[2, 5, 9, 12, 13, 15, 16, 17, 18, 19]
[2, 4, 5, 6, 7, 9, 13, 16, 20]
[1, 2, 5, 9, 10, 11, 12, 13, 15, 20]
Output 1:
[2, 5, 9, 13]
[16]
[12, 15, 16, 20]
[3, 8, 14]

Explanation:
1.Given the three sets, you can see that the students numbered '2', '5', '9', and '13' play all the three sports. 
2. The student numbered '16' plays cricket and football but doesn't play hockey. 
3. The students numbered '12' and '15' play cricket and hockey, the student numbered '16' plays cricket and football and the student numbered '20' plays football and hockey.  Hence, the students who play exactly two sports are 12, 15, 16, and 20.
4. As you can see, the students who play none of the sports are 3, 8, and 14. '''

# Read the three input lists, i.e. 'C', 'F', and 'H'.
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
C = input_list[0]
F = input_list[1]
H = input_list[2]

# Convert the given lists to sets as it is easier to perform the given operations
# on sets
C = set(input_list[0])
F = set(input_list[1])
H = set(input_list[2])

# Perform an '&' operation between the three sets to find out the students who play
# all the three sports. Finally, convert it into a list, apply the sorted() function
# and print the resultant list.
print(sorted(list(C & F & H)))

# The following opeartion gives the students who play only Cricket and Football.
# Note that only (C & F) also contains the students who play all the three sports
# and hence, we need to subtract (C & F & H) from it.
print(sorted(list((C & F) - (C & F & H))))

# The students who play exactly three sports can be given by the following expression
# (C & F) gives the students who play cricket and football, (F & H) gives the students
# who play football and hockey, and (C & H) gives the students who play cricket and
# hockey. Performing an 'OR' operation ('|') between the three will give the students
# who play a minimum of two sports and finally subracting (C & F & H) will give the 
# list of students who play exactly two sports.
print(sorted(list(((C & F) | (F & H) | (C & H)) - (C & F & H))))

# As the students are numbered from 1 to 20, the whole set of students can be defined
# by creating a set containing all the numbers from 1 to 20, using range. Finally,
# you can subract (C | F | H), from the created set to get all the students who don't
# play even a single sport.
print(sorted(list(set(range(1,21)) - (C | F | H))))
