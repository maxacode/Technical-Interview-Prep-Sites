
# https://www.youtube.com/watch?v=CG7AYoFLN2o

# Greedy Option - Not a optimal solution

mass = [10, 20, 15, 30,5]
worth = [30, 60, 60, 20]
maxMass = 80


# def knapSack(mass, worth, maxMass):
#    # print(sorted(mass, reverse=True, key=lambda item:item if item <= maxMass else False))
#     leftMass = maxMass
#     items = {}
#     sortedReverseMass = sorted([i for i in mass if i <= maxMass], reverse=True)
#     print(sortedReverseMass)

#     for index, value in enumerate(sortedReverseMass):
#         #print(worth[index])
#         #Makes it where i can have multiple of teh same items
#         while True:
#             if value <= leftMass:
#                 if value not in items:
#                     items[value] = 0
#                 items[value] += 1
#                 leftMass -= value
#                 print(items)
#             else:
#                 break
        

# more optimal - Sorty based on Mass/Worth since that gives the "weighted approach"

def knapSack(mass: list[int], worth: list[int], maxMass: int)-> list[int, str]:
   # print(sorted(mass, reverse=True, key=lambda item:item if item <= maxMass else False))
    leftMass = maxMass
    items = {}
   # print(sorted(mass,key=lambda mass:worth/mass))
   # for x in range(0, len(mass)-1):
 #       print(worth[x]/mass[x])
    sortedWeighted = [worth[x]/mass[x] for x in range(0, len(mass)-1)]
    print(sortedWeighted)

    # sortedReverseMass = sorted([i for i in mass if i <= maxMass], reverse=True)
    # print(sortedReverseMass)

    # for index, value in enumerate(sortedReverseMass):
    #     #print(worth[index])
    #     #Makes it where i can have multiple of teh same items
    #     while True:
    #         if value <= leftMass:
    #             if value not in items:
    #                 items[value] = 0
    #             items[value] += 1
    #             leftMass -= value
    #             print(items)
    #         else:
    #             break
        


knapSack(mass, worth, maxMass)