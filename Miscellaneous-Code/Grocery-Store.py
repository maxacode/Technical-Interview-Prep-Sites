groceries = [('apples', 2.00), ('oranges', 3.00), ('milk', 3.00), ('bread', 5.00)]
totalItems = 0
totalCost = 0
purchased = {}

for x in groceries:
    itemCount = input(f"How many {x[0]} do you want to buy:  ")
    totalCost += x[1] * int(itemCount)
    totalItems += int(itemCount)
    purchased[x[0]] = int(itemCount)

    print(f"\nThe total cost of {x[0]} is ${(x[1] * int(itemCount))}\n")
    
print(f"\nTotal Cost of your {totalItems} items of {purchased} Groceries: {totalCost} \n")

print(f"The Total Cost of your Groceries: {str(totalCost)} \n The Total Items of your Groceries: {str(totalItems)}")

# itemCount = [x[1] * int(input(f"How many {x[0]} do you want to buy:  ")) for x in groceries]
# print ("The total cost of your groceries is ${}".format(sum([x[1] * int(itemCount) for x in groceries])))