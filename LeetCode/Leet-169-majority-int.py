""""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
Input: nums = [3,2,3] Output: 3
Input: nums = [2,2,1,1,1,2,2] Output: 2
"""
def getMajority(nums: list[int]) -> int:
    from collections import Counter
    #Option 1
    # counterNums = Counter(nums)
    # return(max(counterNums, key =counterNums.get ))
    #option 2
    # s = Counter(nums).most_common()
    # print(s[0][0])
    # Option 3
    # non_duplicate = list(set(nums))
    # for i in non_duplicate:
    #     if nums.count(i) > (len(nums)/2):
    #         return i
    #OPtion 4
    dictNums = Counter(nums)
    return max(dictNums, key=dictNums.__getitem__)


nums = [3,2,3]
print(getMajority(nums)) # 3
nums = [2,2,1,1,1,2,2]
print(getMajority(nums)) # 2
nums = [3,3,4]
print(getMajority(nums)) # 3
