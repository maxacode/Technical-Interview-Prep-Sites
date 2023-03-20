# Anagram 
# Given an array of strings goup anagram togethr and return in any order
# ex: strs =["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import defaultdict
def groupAnagram(strs: list[str]) -> list[list[str]]:
    str_map = defaultdict(list)   
    result = []
    for s in strs: 
        sorted_s = tuple(sorted(s))
#        if sorted_s not in str_map:
 #           str_map[sorted_s] = []    
        str_map[sorted_s].append(s)
    for value in str_map.values():
        result.append(value)
    return result











strs =["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(strs))