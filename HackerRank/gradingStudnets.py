

"""
def gradingStudents(grades):
    print(a)
    for x in a:
        if x <= 37:
            print(x)
        elif ((x+2)/5).is_integer():
            print(x+2)
        elif ((x+1)/5).is_integer():
            print(x+1)
        else: 
            print(x)
    

a = [73, 67, 38, 33]
 #   75  67  40  33

print(gradingStudents(a))
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(a):
    # Write your code here
    solu = []
    for x in a:
        if x <= 37:
            solu.append(x)
        elif ((x+2)/5).is_integer():
            solu.append(x+2)
        elif ((x+1)/5).is_integer():
            solu.append(x+1)
        else: 
            solu.append(x)
    #print(solu)
    return(solu)

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))



    

"""

HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
Examples

 round to  (85 - 84 is less than 3)
 do not round (result is less than 40)
 do not round (60 - 57 is 3 or higher)
Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

Function Description

Complete the function gradingStudents in the editor below.

gradingStudents has the following parameter(s):

int grades[n]: the grades before rounding
Returns

int[n]: the grades after rounding as appropriate
Input Format

The first line contains a single integer, , the number of students.
Each line  of the  subsequent lines contains a single integer, .

Constraints

Sample Input 0

4
73
67
38
33
Sample Output 0

75
67
40
33
Explanation 0

image

Student  received a , and the next multiple of  from  is . Since , the student's grade is rounded to .
Student  received a , and the next multiple of  from  is . Since , the grade will not be modified and the student's final grade is .
Student  received a , and the next multiple of  from  is . Since , the student's grade will be rounded to .
Student  received a grade below , so the grade will not be modified and the student's final grade is .

"""