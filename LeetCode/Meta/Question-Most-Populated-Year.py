# # Given birth years and death years - which year had the most population of people. 


# dates = ((1901, 2000), (1903, 1991), (1920,2010), (1801, 1824), (1913, 1951), (1220,1310), (1913, 1951))

# #sample answer 1901: 1, 1902: 1, 1903: 2, 1904:2 ... 1920:3 ... 1991:3 1992:2
# minYear = min(min(dates))
# #print(minYear)

# maxYear = max(max(dates))
# #print(maxYear)

# allYears = {}
# for x in range(minYear, maxYear+1):  #1901
#     allYears[x]  = 0
#     for person in dates:
#         if  x >= person[0] and x <= person[1]: 
#            # print(f"{person} is Alive in {x}")
#             allYears[x] += 1


 # #print(allYears)
# #print(min(allYears, key = allYears.get))
# print(max(allYears, key = allYears.get))
# highestNum = max(allYears.values())
# #print(highestNum)
# print([k for k, v in allYears.items() if v == highestNum ])

### !!! This works and gives this:
## 1920
## [1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951]


################## ANother way 


# # Given birth years and death years - which year had the most population of people. 
# Method two, any year thats is the highest. so i can only check the years when peole are born

dates = ((1901, 2000), (1903, 1991), (1920,2010), (1801, 1824), (1913, 1918), (1220,1310), (3003, 3050))

# #sample answer 1901: 1, 1902: 1, 1903: 2, 1904:2 ... 1920:3 ... 1991:3 1992:2

# looping though each birth year and checking if other peole hav ebeen alive, if yes +1 if not pass. Chekcing Birth and Death
allYears = {}

for index, currentYear in enumerate(dates):
    allYears[currentYear[0]] = 0
    for nextYear in range(0, len(dates)):
        if dates[nextYear][0] <= currentYear[0] and dates[nextYear][1] >= currentYear[0]:
            allYears[currentYear[0]] += 1

print(allYears)
print(max(allYears, key = allYears.get))

# WOrks!
# sample output
# {1901: 9, 1903: 18, 1920: 27, 1801: 9, 1913: 27, 1220: 9, 3003: 9, 1914: 36}
# 1914