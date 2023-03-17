

## 242. Valid Anagram

# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
    
#     sDict = {}
#     tDict = {}

#     for letter in s:
#         sDict[letter] = s.count(letter)
#     for letter in t:
#         tDict[letter] = t.count(letter)

#     for index, key in enumerate(sDict):
#         #print(key, sDict[key])
#         if key not in tDict.keys():
#             print(s, t)
#             return False
#         elif tDict[key] != sDict[key]:
#             return False
#     else:
#         return True
 
# # print(isAnagram("anagram","nagaram"))
# print(isAnagram("aacc","ccac"))
# # print(isAnagram("oer","roe"))
# # print(isAnagram("batters","battter"))


"""
for letter in t:
            if t.count(letter) != s.count(letter):
                return False
        return True
        
        """

from collections import Counter
# def isAnagram(word1, word2):
#     print(collections.Counter(word1))
#     print(collections.Counter(word2))
#     return True if collections.Counter(word1) == collections.Counter(word2) else False

def isAnagram(word1, word2):
    Counter(word1)
    print(Counter(word1))
    print(Counter(word2))
    return Counter(word1) == Counter(word22)

print(isAnagram("anagram","nagaram"))
print(isAnagram("aacc","ccac"))
print(isAnagram("oer","roe"))
print(isAnagram("battert","battter"))