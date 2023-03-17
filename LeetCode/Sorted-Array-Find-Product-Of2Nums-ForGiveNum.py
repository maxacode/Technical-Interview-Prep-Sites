"""Given a sorted aray of numbers find the product of two numbers closces to a given number
https://www.youtube.com/watch?v=oxefDeTNbeY&list=PLn1uch862uBhLHQGCgivcOgbicVo8ngXc&index=7
ex: 
input 2,6, 7 target 30
output 6, 7

ex:
input 1,3,4,6,7 target 10
output 3,4

Idea is to loop thorugh index 1 * index2 then 3 etc. Subtract from Target then make positive and smallest difference wins. 

# """

# def calcTarget(input: list[int], target: str) -> list[int,int]: 
#     tempWin = []
#     tempSum = float('inf')
#     for x in range(0, len(input)-1):
#         for y in range(x+1,len(input)-1):
#             intX = input[x]
#             intY = input[y]
#             if input[x] * input[y] == 0:
#                 continue
#             if abs((target) - (input[x]*input[y])) <= tempSum:
#                 tempWin = (input[x],input[y])
#                 tempSum = abs((target) - (input[x]*input[y]))

#     return tempWin


# print(calcTarget([1,3,4,6,7], 20))

def calcTarget(input: list[int], target: str) -> list[int,int]: 
    tempWin = []
    tempSum = float('inf')
    for x in range(0, len(input)-1, -1):
        for y in range(x+1,len(input)-1):
            intX = input[x]
            intY = input[y]
            if input[x] * input[y] == 0:
                continue
            if abs((target) - (input[x]*input[y])) <= tempSum:
                tempWin = (input[x],input[y])
                tempSum = abs((target) - (input[x]*input[y]))

    return tempWin


print(calcTarget([1,3,4,6,7], 20))