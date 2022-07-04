#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    print(arr)
    sum1 = 0
    sum2 = 0 
    y = 0
    for x in range(0, len(arr)):
        sum1 += (arr[x][x])
    for z in range(len(arr)-1, -1,-1):
        print(f"Z is : {z}")
        
        print(f"Sum2 is: {arr[y][z]}")
        sum2 += (arr[y][z])
        y += 1
         

    print(sum1,sum2)
    return(abs(sum1-sum2))

if __name__ == '__main__':


    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]] #15 11+5+-12 = 4 sum2 4+5+10
    arr2 = [[-1, 1, -7, -8,],[-10, -8, -5, -2],[0, 9, 7, -1],[4, 4, -2, 1]]
    result = diagonalDifference(arr2)
    print(result)