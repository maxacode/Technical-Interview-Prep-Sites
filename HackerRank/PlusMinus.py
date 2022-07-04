#!/bin/python3

from itertools import count
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    k = 0 

    test = len([i for i in arr if i > k])
    testSum = test/len(arr)
    print("{:.6f}".format(round(testSum, 6)))

    test = len([i for i in arr if i < k])
    testSum = test/len(arr)
    print("{:.6f}".format(round(testSum, 6)))

    test = len([i for i in arr if i == k])
    testSum = test/len(arr)
    print("{:.6f}".format(round(testSum, 6)))

 
   # print(round(posSum, 6),neg, zero)

if __name__ == '__main__':
   # n = int(input().strip())

   # arr = list(map(int, input().rstrip().split()))
    arr = -4, 3, -9, 0, 4, 1
    plusMinus(arr)
