"""
Array pair sum 
Iven an inter array output all the unuqi pairs that sum up to ta specific value k.
so the input
pair_sum([1,3,2,2],4)
wourt retunr 2 pairs: (1,3) & (2,2)

https://youtu.be/p65AHm9MX80?t=4031

"""

# def pair_sum(array, k):
#     print("New Run")
#     array.sort()
#     for x in range(len(array)):
#         if (array[x] + array[x-1]) % k == 0:
#             print(array[x],array[x-1])


# def pair_sum(array, k):
#     if len(array) < 2:
#         return ("Array to Small! Try again")
    
#     seen = set()
#     output = set()

#     for num in array():
#         target = k - num

#         if target not in seen:
#             seen.add(num)
#         else:
#             output[target]
            
             
#Solution from youube vid.

 


def pair_sum(array, k):
    if len(array) < 2:
        return print("Small")

    seen = set()
    output = set()

    for num in array:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
            print(output)
            # output.add((2,2))
            # print(output)

    print(list((map(str, list(output)))))
   

print(pair_sum([1,3,2,2],4))

#print(pair_sum([1,3,2,4,0,2],4))