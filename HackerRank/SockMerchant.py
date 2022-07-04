#Matching socks


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

""" complex solution
def sockMerchant(n, ar):
    # Write your code here
    #print(n, ar)
    numOfPairs = 0
    pairs = []
    ar2 = list(ar)
    print(ar2)
    try:
        for x in range(0, len(ar)):
            print(f"X now {ar[x]}")
        # print()
            #del ar2[10]
            ar2.remove(ar[x])
            print(ar2)
            if ar[x] in ar2:
                print(f"in list {ar[x]}")
                numOfPairs +=1
                ar2.remove(ar2[x])
                print(f"AR2 after Remove of {ar2} and AR: {ar}")
        return(numOfPairs)
     
    except Exception as e:
        print(e)
        return(numOfPairs)

        exit()
"""
"""
def sockMerchant(n, ar):
    dic = {}
    for i in ar:
        dic[i] = ar.count(i)
        print(dic)
    total = sum([math.floor(count/2) for count in dic.values()])
    return total

"""

def sockMerchant(n, ar):
    sum = math.floor(3/2)
    print(sum)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = 9
    n = 10
    ar = 1, 1, 3, 1, 2, 1, 3, 3, 3, 3
    #ar = 10, 20,20, 10, 10, 30, 50, 10, 20


    result = sockMerchant(n, ar)
    print(result)
    #fptr.write(str(result) + '\n')

#    fptr.close()
