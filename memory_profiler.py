
 

# create a random dictionary of words and their definitions
import profile


ports_protocols = {
        "21": "FTP",
        "22": "SSH",
        "23": "TELNET",
        "25": "SMTP",
        "53": "DNS",
        "80": "HTTP",
        "443": "HTTPS",
        "3306": "MYSQL",
        "5432": "POSTGRESQL"}

from memory_profiler import profile
import timeit

@profile(precision=2)
def create_dictionary():
    words = ['apple', 'banana', 'orange', 'coconut', 'strawberry', 'lime', 'grapefruit', 'lemon', 'kumquat', 'blueberry', 'melon']
    dictionary = {}
    for word in words:
        definition = word + " is a fruit."
        dictionary[word] = definition
    return dictionary   # return the dictionary


print(timeit.timeit("create_dictionary()", setup="from __main__ import create_dictionary",number=1))

# for x in dict1:
#     print(x, dict1[x])