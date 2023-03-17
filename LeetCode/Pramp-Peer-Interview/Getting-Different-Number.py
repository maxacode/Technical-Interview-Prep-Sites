
"""Getting a Different Number

Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4 

Constraints:

    [time limit] 5000ms

    [input] array.integer arr
        1 ≤ arr.length ≤ MAX_INT
        0 ≤ arr[i] ≤ MAX_INT for every i, 0 ≤ i < MAX_INT

    [output] integer
"""
# def get_different_number(arr):
#   # SMallest non integer in teh array 
#   # example: 0, 2, 3, 5 
#   # Linear search so O(n) maybe could make it Log(n)? 
#     n=len(arr)
#     s=set(arr)

#     for i in range(0,n):
#         if i not in arr:
#             return i
#     return

def get_different_number(arr):
    for x in range(max(arr)):
        if x not in arr:
            print(x)
            return x
        
print(get_different_number([0,1,2,2,4,3,5, 44,144]))

print(get_different_number([3,4,-1,0]))
 

# Peer attempt
'''            i
input:  arr = [0, 1, 2, 3]  array 

output: 4                   integer 
                i
                2
input: arr=[0,1,3,5,99, 342, 5312, 3535, 23523, 23523, 23432]
output: 1

smallest=max(arr)

arr[i]+1

'''


def get_different_number(arr):
  arr= sorted(arr)
 
  
  for i in range(len(arr)):
   if i <arr[i]:
      return i
  
  
      
  return arr[-1]+1






