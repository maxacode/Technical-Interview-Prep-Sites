# The sort() function will modify the list it is called on. 
# The sorted() function will create a new list 
# containing a sorted version of the list it is given.

list2 = [4,8,2,1]
list2.sort()
#--> list = [1,2,4,8] now

list3 = [4,8,2,1]
new_list = list3.sorted()
#--> list = [4,8,2,1], but new_list = [1,2,4,8]