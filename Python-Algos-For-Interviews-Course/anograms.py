# if 2 given strings are Anograms = God Dog = True.. Not couting Spaces and Capitilziation 
# ex 2: clint eastwood  = old west action = True

# string1 = "God Is Good"
# string2 = "Dogigoos d"

# #test 2
# string1 = "clint eastwood"
# string2 = "old west action"


# def anogramTest(string1, string2):
#     string1 = string1.lower().replace(' ', '')
#     string2 = string2.lower().replace(' ', '')
#     if len(string1) >= len(string2):
#         longString = string1
#     else:
#         longString = string2
#     for x in longString:
#         if string1.count(x) == string2.count(x):
#             #print(string1.count(x))
#             if x == longString[-1]:
#                 return print("True Anogram")

#         else:

#             return print("False")


# anogramTest(string1, string2)

# #test 2
# string1 = "clint eastwood f"
# string2 = "old west action jjkk"


# #Same test just returns what other Chars and count is needed to make true. 
def anogramTestToMakeTrue(string1, string2):
    string1 = string1.lower().replace(' ', '')
    string2 = string2.lower().replace(' ', '')
    chars = {}
    
    # if len(string1) >= len(string2):
    #     longString = string1
    # else:
    #     longString = string2

    for x in max(len(string1), len(string2)):
        if string1.count(x) == string2.count(x):
            #print(string1.count(x))
            if x == longString[-1]:
                return print(f"True Anogram: {string1} | {string2}")

        else:
            chars[x] = (string1.count(x) + string2.count(x))
            if x == longString[-1]:
                return print(chars)

string1 = "clint eastwood"
string2 = "old west action"

print(max(string1, string2))
anogramTestToMakeTrue(string1, string2)

string1 = "god"
string2 = "dog"

anogramTestToMakeTrue(string1, string2)

# #test 3

# Create an algorithm that given 2 strings returns "True" if they are Anograms else False  Not couting Spaces and Capitilziation 
# Ex: string1: God String2: Dogs = True..
# ex 2: clint eastwood  = old west action = True


# def anogramEasyiestWithSet(string1, string2):
#     return print((sorted(string1.lower().replace(' ', ''))) == (sorted(string2.lower().replace(' ', ''))))
     


# string1 = "Dogs"
# string2 = "God"

# anogramEasyiestWithSet(string1, string2) # Should be False

# string1 = "clint eastwood"
# string2 = "old west action"
# anogramEasyiestWithSet(string1, string2) # Should be true 






# #Test 4 - best solution:

# def anogramBestSolution(s1, s2):
#     s1, s2 = s1.lower().replace(' ', ''),s2.lower().replace(' ', '')
#     print(s1, s2)
#     if len(s1) != len(s2):
#         return print(False)

#     count = {}

#     for x in s1:
#         if x in count:
#             count[x] +=1 
#         else:
#             count[x] = 1
#     print(count)
#     for x in s2:
#         if x in count:
#             count[x] -=1
#         else:
#             count[x] = 1
#     print(count)

#     for x in count:
#         # print(count[x])
#         if count[x] != 0:
#             return print(False)
#     return print(True)
  

# string1 = "Dogs"
# string2 = "Gods"

# anogramBestSolution(string1, string2) # Should be False

# string1 = "clint eastwood"
# string2 = "old west action"
# anogramBestSolution(string1, string2) # Should be true 