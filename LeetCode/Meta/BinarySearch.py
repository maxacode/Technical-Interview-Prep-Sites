# # Create a binary search algorythm 
# # Given an assorted array give the position of X

# array = 1, 4, 5, 9, 12, 24, 34, 52, 55, 88, 99, 113, 342, 513, 522, 555, 566, 599, 611, 622, 644, 699, 710, 725,792, 810,823
# find = 792


# start = 0
# end = len(array) - 1
# mid = (start + end) // 2
# loops = 0
# print(start, mid, end)
# while start <= end:
#     loops += 1
#     print(loops)
#     if find == array[start]:
#         print("start")
#         print(f"{find} is located at {start}")
#         break
#     elif find == array[end]:
#         print("end")
#         print(f"{find} is located at {end}")
#         break
#     elif find == array[mid]:
#         print("mid")
#         print(f"{find} is located at {mid}")   
#         break
    
#     if find >= array[mid]:
#         start = mid + 1
#         mid = (start + end) // 2
#     elif find <= array[mid]:
#         end = mid - 1
#         mid = (start + end) // 2


###### anothe rway
# Create a binary search algorythm 
# Given an assorted array give the position of X

array = 1, 4, 5, 9, 12, 24, 34, 52, 55, 88, 99, 113, 342, 513, 522, 555, 566, 599, 611, 622, 644, 699, 710, 725,792, 810,823
find = 725

count = 0
for x in range(0, len(array)-1):
    count += 1
    if find == array[x]:
        print(count)
        print(find)
        print(x)


start = 0
end = len(array) - 1
mid = (start + end) // 2
loops = 0
print(start, mid, end)
while start <= end:
    loops += 1
    print(loops)
    # if find == array[start]:
    #     print("start")
    #     print(f"{find} is located at {start}")
    #     break
    # elif find == array[end]:
    #     print("end")
    #     print(f"{find} is located at {end}")
    #     break
    if find == array[mid]:
        print("mid")
        print(f"{find} is located at {mid}")   
        break
    
    if find >= array[mid]:
        start = mid + 1
        mid = (start + end) // 2
    elif find <= array[mid]:
        end = mid - 1
        mid = (start + end) // 2
