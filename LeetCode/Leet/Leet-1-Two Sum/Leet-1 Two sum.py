"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
https://www.youtube.com/watch?v=oxefDeTNbeY&list=PLn1uch862uBhLHQGCgivcOgbicVo8ngXc&index=7 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

def calcTarget(input: list[int], target: str) -> list[int,int]: 
    tempWin = []
    tempSum = float('inf')
    for x in range(0, len(input)):
        for y in range(x+1,len(input)):
            intX = input[x]
            intY = input[y]
            if input[x] * input[y] == 0:
                continue
            if abs((target) - (input[x]+input[y])) <= tempSum:
                tempWin = (x,y)
                tempSum = abs((target) - (input[x]+input[y]))

    return tempWin


print(calcTarget([2,7,11,15], 9))
print(calcTarget([3,2,4], 6))
print(calcTarget([3,3], 6))
