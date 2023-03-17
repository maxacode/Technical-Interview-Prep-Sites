
def testFunc(inputVar: list[int], target: int)-> list[int]:
    # Take a list and return all int more than Target
    matrix = [x for x in inputVar if x >= target]
    print(matrix)
    output = [num for num in inputVar if num >= target]
    print(output)
    return output

print(testFunc([0,3,4,5], 5))

testList = [1, 2, 3, 4, 5]
print(testList)

testList[0], testList[4] = testList[4], testList[0] 
print(testList)