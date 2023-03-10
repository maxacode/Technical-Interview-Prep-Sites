# Looping
nums = [1,2,3,4,5,6,7,8,9,10]
square_nums = [singleNum for singleNum in nums if singleNum <= 5]
print(nums)
print(square_nums)

################################################################################################

# If Statmen
age = 20
if age < 18:
    age_group = "Minor"
else:
    age_group = "Adult"
print(age_group)

age = 20
age_group = "Minor" if age < 18 else "Adult"
print(age_group)

################################################################################################################################

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
