"""
Given an array with mosty positive non zero numbers find the 2 integers of Sum Ke

ex: 1,2,5,6,9,10 k= 3 = answer = 1,2 or k= 11 answer = 5,6

"""

def findSum(values: list[int], target: int) -> list[int]:
    #Looping through all values

    allPairs = {}
    for indvValue in values:
        #Subtracking indvValue from Target and checking if remainder in values
        remainder = target - indvValue
        if remainder in values:
            allPairs[indvValue] = remainder
    
    if len(allPairs) == 0:
        return ("No valid Pairs")

    return allPairs






values = [1,2,5,6,9,10]
target = 11
print(findSum(values, target))
target = 30
print(findSum(values, target))