#!/bin/python3

import math
import os
import random
import re
import sys
from telnetlib import EC

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#        
"""
def jumpingOnClouds(c):
        print(c)
        jumps = 0
        jump = 0
        for index, elem in enumerate(c):
            print(f"Jump: {jump}")
            if jump == 1:
                jump = 0
               # print(f"Start for index: {index}")
                continue
            print(f"Start for index: {elem}")
            if elem == 2:
                # index += 2
                jumps += 1
                jump = 1
                print(f"Plus 2 index: {index} elem: {elem}") 
            elif elem == 4:
                jumps += 1
                jump = 1
                print(f"Plus 2 index: {index} elem: {elem}")
            elif elem == 8:
                jumps += 1
                jump = 1
                print(f"Plus 2 index: {index} elem: {elem}")

        return(jumps)
"""
"""
def jumpingOnClouds(c):

    # Write your code here
    jumps = 0
    jump = 0
    try: 
        for index, elem in enumerate(c):   
           #if elem == 1:
              #  continue
            if jump == 1:
                jump = 0
                continue
               
            print(f"Current Cloud: index: {index} number: {elem}")
            print(f"Index Plus 1 {c[index+1]}")
            print(f"index Plus 2: {c[index+2]}")
            if elem == 0 and c[index+1] != 0 and c[index+2] != 1:
                
                print(f"Jumped Two {index+2}")
                jumps += 1
                jump = 1
                print(f"Jumps: {jumps}")
            elif elem == 0 and c[index+2] != 1:
                
                print(f"Jumped two {index+2}")
                jumps += 1
                jump = 1
                print(f"Jumps: {jumps}")

            elif elem == 0 and c[index+1] != 1:
                
                print(f"Jumped one {index+1}")
                jumps += 1

            else:
                print("---No Jumps")
 
    except Exception as e:
        print(e)
        return(jumps)
"""
""" 
def jumpingOnClouds(c):
    x = 0 
    jumps1 = 0
    jumps2 = 0
    try:
        while x < len(c):
            if c[x] == 0 and c[x+2] != 1:
                print(f"Jumped Two {x+2}")
                x += 2
                jumps1 += 1
                print(f"Jumps: {jumps}")
            if c[x+1] != 1:
                print(f"Jumped One {x+1}")
                x += 1
                jumps += 1
            else:
                x += 1
        return(jumps)
    except:
        
        return(jumps)
"""
def jumpingOnClouds(c):
    x = 0 
    singleJump = {}
    doubleJump = {}
    try: 
        while x < len(c):
            if c[x] == 0 and c[x+1] == 0:
                print("Jumped Once: ")
                singleJump[x+1] = x
                print(singleJump)
                x += 1
                continue
            if c[x+2] == 0:
                print("Jumped two")
                doubleJump[x+2] = x
                print(doubleJump)
                x += 2
                continue
    except:
        print(f"Single Jumps: {singleJump}")
        print(f"Double Jumps: {doubleJump}")
if __name__ == '__main__':
    c = [0,0,1,0,0,1,0] #1,3,4,6
    c2 = [0,0,0,0,1,0] #2,3,5
    c3 = [1,2,3,4,5,6,7,8,9]
    c4 = [0, 0, 0, 1, 0, 0] #2,4,5
    c5 = 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0 
    c6 = 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, # 1,3 5 6 8 9 
    result = jumpingOnClouds(c5)
    print(result)