    
  
  # your code goes here

"""

  Flatten a Dictionary

A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

If a certain key is empty, it should be excluded from the output (see e in the example below).

Example:

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }

Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.

Constraints:

    [time limit] 5000ms
    [input] Dictionary dict
    [output] Dictionary

"""

"""
for index, value in enumerate(dictInput):
      # Check this later - checking if Value ex 1 is not a dictionary.
      
      if value not dict:
          output[dictInput.keys[index]] = value
"""

# Keyset

def flatten_dictionary(dictInput):
    output = {}
    
    helperFuncRecursion("", dictInput, output)
    return output
  
# https://www.youtube.com/watch?v=PtJ6APpEhOU

# def helperFuncRecursion(tempKey, dictInput, output):
  
#     for key,value in dictInput.items():
#     # key = key1 | value = 1
#         if not isinstance(value, dict):
#             tempKey =  tempKey + key
#             output[key] = value
#             del dictInput[key]
#             print(output)
#         tempKey = key + "."
#         helperFuncRecursion(tempKey, dictInput, output)
          
dictOut = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

def helperFuncRecursion(tempKey, dictOut, output):
    for key in dictOut.keys():
        value = dictOut.get(key)
        
        if not isinstance(value, dict):
            if tempKey == None or tempKey == "":
                output[key] = value
            else:
                output[tempKey+"."+key] = value
                print(f"103 OUTPUT {output}")
        else:
            if tempKey == None or tempKey == "":
                helperFuncRecursion(key, value, output)
            else:
                helperFuncRecursion( tempKey +"." + key, value, output)
                print(f"106 Output {output}")

print(flatten_dictionary(dictOut))




"""
ANSWER

Flatten a Dictionary

A recursion is natural choice for this kind of problem. We iterate over the keys in dict and distinguish between two cases: If the value mapped to a key is a primitive, we take that key and simply concatenate it to the flattened key we created up to this point. We then map the resultant key to the value in the output dictionary. If the value is a dictionary, we do the same concatenation, but instead of mapping the result to the value in the output dictionary, we recurse on the value with the newly formed key.

Pseudocode:

function flattenDictionary(dict):
    flatDictionary = {}
    flattenDictionaryHelper("", dict, flatDictionary)

    return flatDictionary


function flattenDictionaryHelper(initialKey, dict, flatDictionary):
    for (key : dict.keyset()):
        value = dict.get(key)

        if (!isDictionary(value)): # the value is of a primitive type
            if (initialKey == null || initialKey == ""):
                flatDictionary.put(key, value)
            else:
                flatDictionary.put(initialKey + "." + key, value)
        else:
            if (initialKey == null || initialKey == "")
                flattenDictionaryHelper(key, value, flatDictionary)
            else:
                flattenDictionaryHelper(initialKey + "." + key, value, flatDictionary)

Time Complexity: O(N), where N is the number of keys in the input dictionary. We visit every key in dictionary only once, hence the linear time complexity.

Space Complexity: O(N) since the output dictionary is asymptotically as big as the input dictionary. We also store recursive calls in the execution stack which in the worst case scenario could be O(N), as well. The total is still O(N).

"""