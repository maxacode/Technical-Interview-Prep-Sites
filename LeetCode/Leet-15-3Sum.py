"""
3Sum 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1: Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

def get3Sum(nums: list[int]) -> list[int]:
    res = []
    nums.sort()
    if len(nums) < 3:
        return res
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r :
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i] ,nums[l] ,nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l - 1]: l += 1
                while l < r and nums[r] == nums[r + 1]: r -= 1
            elif s < 0 :
                l += 1
            else:
                r -= 1
    return res  
  
    # nums.sort()
    # print(nums)
    # allSums = []
    # for x in range(len(nums)-2):
    #     start,end = 0, len(nums) - 1
    #     tempSum = nums[start] + nums[end]
    #     if tempSum + nums[x] == 0:
    #         allSums.append([nums[start], nums[end], nums[x]])
        
    #     while start<end:
    #         tempSum = nums[start] + nums[end]
    #         if tempSum + nums[x] == 0:
    #             allSums.append([nums[start], nums[end], nums[x]])
    #         if nums[x] < 0:
    #             if tempSum > nums[x]:
    #                 end -= 1
    #             else:
    #                 start += 1
    #         else:
    #             if tempSum > nums[x]:
    #                 start +=1

    #             else:
                    #end -=1

 #   return allSums
nums = [-1,0,1,2,-1,-4]
#[-4, -1, -1, 0, 1, 2]
print(get3Sum(nums))