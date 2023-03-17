'''
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

Example 1:
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
 
'''

# nums = [1,5,0,3,5,4,3,2,4,30,21,231,123,12,421,4,51,523,13,]

# def makeZero(nums):
#     s = set(nums)
#     print(s)
#     return len(s) -1 if 0 in s else len(s)
# #     if 0 in s:
# #         return len(s) - 1
# #     else:
# #         return len(s)

# print(makeZero(nums))

'''
Given an interger array and a number k, ouput all pairs tha tum up to tk

# '''

# allSumsDict = {}

# def allSums(nums, k):
#     pass
#     newNums = list(set([num for num in nums if num <= k]))
#     #nums = for set(nums) in 

#     for currIndex in range(0, len(newNums)):
#         for nextIndex in range(currIndex+1, len(newNums)):
#             if newNums[currIndex] + newNums[nextIndex] == k:
#                 allSumsDict[newNums[currIndex]] = newNums[nextIndex] 
#                 print(allSumsDict)

#     # for indivNum in newNums:
#     #     remainder = k - indivNum
#     #     newNums.remove(indivNum)
#     #     if remainder in newNums:
#     #         allSumsDict[indivNum] = remainder

#     return allSumsDict

# test1 = 1,3,2,3,2,5,46,6,7,4
# k = 5
# print(allSums(test1, k))


allSumsDict = {}

def allSums(nums, k):
    pass
    newNums = list(set([num for num in nums if num <= k]))
    #nums = for set(nums) in 
  #  for currIndex in range(0, len(newNums)): for nextIndex in range(currIndex+1, len(newNums)): if newNums[currIndex] + newNums[nextIndex] ==k : print(newNums[currIndex], newNums[nextIndex])
    print([(newNums[currIndex], newNums[nextIndex]) for currIndex in range(0, len(newNums)) for nextIndex in range(currIndex+1, len(newNums)) if newNums[currIndex] + newNums[nextIndex] ==k])

   # print(test)
    print('test above')
    # for currIndex in range(0, len(newNums)):
    #     for nextIndex in range(currIndex+1, len(newNums)):
    #         if newNums[currIndex] + newNums[nextIndex] == k:
    #             allSumsDict[newNums[currIndex]] = newNums[nextIndex] 
    #             print(allSumsDict)

    # for indivNum in newNums:
    #     remainder = k - indivNum
    #     newNums.remove(indivNum)
    #     if remainder in newNums:
    #         allSumsDict[indivNum] = remainder

    return allSumsDict

test1 = 1,3,2,3,2,5,46,6,7,4
k = 5
print(allSums(test1, k))
