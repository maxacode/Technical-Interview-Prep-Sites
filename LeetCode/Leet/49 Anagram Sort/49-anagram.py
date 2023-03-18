"""
Given an array of strings goup anagram togethr and return in any order

ex: strs =["eat", "tea", "tan", "ate", "nat", "bat"]

"""

#f = open("user.out", "w");[print(json.dumps(list(reduce(lambda res, s: res[str(sorted(s))].append(s) or res, json.loads(line.rstrip()), defaultdict(list)).values())), file=f) for line in stdin];exit()

# tanle - 2023
from collections import defaultdict
def groupAnagram(strs: list[str]) -> list[list[str]]:
    #str_map2 = defaultdict(list)
    #str_map = {}
    #print(type(str_map2))
    print(type(str_map))
    
    
    print(str_map)
    result = []

    for s in strs:
        sorted_s = tuple(sorted(s))
        if sorted_s not in str_map:
            str_map[sorted_s] = []
       
        str_map[sorted_s].append(s)

        #str_map[sorted_s].append(s)

    for value in str_map.values():
        result.append(value)

    return result











strs =["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(strs))