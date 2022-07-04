#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    elevation = 0
    valleys = 0
    for x in path:
        
        
        if x == "U":
            elevation += 1
        elif x == "D":
            elevation -= 1
 
        if x == "U" and elevation == 0:
     #       print("Up from Valley")
            valleys += 1
        
    #    print(elevation)
    return(valleys)

if __name__ == '__main__':
   
    steps = 8

    path = "UDDDUDUU"

    result = countingValleys(steps, path)
    print(result)