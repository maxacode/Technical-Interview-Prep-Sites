#!/bin/python3

import math
import os
import random
import re
import sys


https://note.nkmk.me/en/python-check-int-float/

"""   
    <p>Given a number  n , for each integer  i &nbsp;in the range from  1 &nbsp;to  n &nbsp;inclusive, print one value per line as follows:</p>

        <li>If  i  is a multiple of both  3  and  5 , print  FizzBuzz .</li>
        <li>If  i  is a multiple of  3  (but not  5 ), print  Fizz .</li>
        <li>If  i  is a multiple of  5  (but not  3 ), print  Buzz .</li>
        <li>If  i  is not a multiple of  3 &nbsp;or  5 , print the value of  i .</li    
"""


 

def fizzBuzz(n):
    #For loop with I var starting from 0 to end of N. 
    for i in range(1,n+1):
        #print(i)
        #Checking if Divisible by 3 and 5:
        div3 = i/3
        div5 = i/5
        if div3.is_integer() and div5.is_integer():
            print(f'FizzBuzz')
            continue
        elif div3.is_integer():
            print(f'Fizz')
            continue
        elif div5.is_integer():
            print(f'Buzz')
            continue
        else:
            print(f'{i}')
            continue
 
fizzBuzz(15)
"""
    1     
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz</pre>
    
    """