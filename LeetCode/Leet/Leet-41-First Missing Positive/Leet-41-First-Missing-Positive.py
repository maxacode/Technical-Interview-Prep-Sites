"""
https://leetcode.com/problems/first-missing-positive/description/
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

"""

class Solution:
    def firstMissingPositive(self, nums):
        n=len(nums)
        s=set(nums)
        for i in range(1,n+2):
            if i not in s:
                return i



test1 = ([7,8,9,11,12,0,1,2,3],[3,4,-1,1,0],[3,4,-1,1])
for x in test1:
    print(Solution.firstMissingPositive(0,x))



