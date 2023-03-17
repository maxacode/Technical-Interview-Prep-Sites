"""
Given an array of intergers ind the largest configuous subarray
ex: -1, -4, 8
output 8
ex 1,1,7,-10
ex: 9 (1+1+7)

https://www.youtube.com/watch?v=lcqTgJCQlFA&list=PLn1uch862uBhLHQGCgivcOgbicVo8ngXc&index=5&t=11s

"""


# def findLargestSum(array: list[int])-> int:
#     tempLarge = float('-inf')

#     for x in range(len(array)):
#         tempIndex = 0
#         for y in range(x, len(array)):
#             tempIndex += array[y]
#             if tempIndex > tempLarge:
#                 tempLarge = tempIndex

#     return f"tempLarge {tempLarge}"

# print(findLargestSum([1,1,7,-10]))

# print(findLargestSum([-1,-4,8]))


"""

def findLargestSum(array: list[int])-> int:
    tempLarge = float('-inf')

    for x in range(len(array)):
        tempIndex = array[x]
        for y in range(x+1, len(array)):
            addInt = array[y] + tempIndex
            if addInt >= tempLarge and addInt >= 0:
                tempLarge = array[y] + tempIndex
                tempIndex += array[y]
            else:
                break

    return f"tempLarge {tempLarge}"
"""

def findLargestSum(array: list[int])-> int:
    tempLarge = float('-inf')

    for x in range(len(array)):
        tempSum = 0 
        for y in range(x, len(array)):
            tempSum += array[y]
            if tempSum >= tempLarge:
                tempLarge = tempSum

    return(tempLarge)


print(findLargestSum([1,1,7,-10]))

print(findLargestSum([-1,-4,8]))

print(findLargestSum([1,1,7,-10, 3, 13,1,-99, 1,4,53,55]))
