"""
Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.
Illustration : A[] = {10, 20, 35, 50, 75, 80} X = =70 i = 0 j = 5
"""

def twoPointers(values:list[int], target: int) -> list[int]:
    # Creating the starting and end index's
    values.sort()
    start = 0
    end = len(values) - 1
    # looping through every value in given list
    for _ in range(0, len(values)):
        # Checking if the sum of values with index start/end is greater than our target if so we will subtract 1 of end index since the end is the largest number else we will add 1 to start
        #if sum's equal then returning indexes
        tempSum = values[start] + values[end]
        if  tempSum == target: return(start, end) 
        if tempSum > target: end -=1 
        if tempSum < target: start +=1

A = [10, 20, 35, 50, 75, 80]
target = 70
print(twoPointers(A, target)) # 0, 3

target = 115
print(twoPointers(A, target)) # 2,5

target = 300
print(twoPointers(A, target)) # None
 