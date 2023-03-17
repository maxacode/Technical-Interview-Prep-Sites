"""
https://www.youtube.com/watch?v=xwf0kBjo79Q&list=PLn1uch862uBhLHQGCgivcOgbicVo8ngXc&index=5



896. Monotonic Array
Easy
2K
63
Companies
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105

"""

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        sort = sorted(nums)
        print(nums)
        print(nums[::-1])
        print(sort)
        return sort == nums or sort == nums[::-1]

print(Solution.isMonotonic(1,(1,2,3,4,5)))

"""
Python3

Runtime
956 ms
Beats
93.32%

Memory
27.6 MB
Beats
97.79%
"""