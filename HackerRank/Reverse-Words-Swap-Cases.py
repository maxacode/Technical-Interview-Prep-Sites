

#!/bin/python3

from curses.ascii import islower
import math
import os
import random
import re
import sys
from turtle import done
 

def reverse_words_order_and_swap_cases(sentence):
    #Spliting each letter into a list
    sentence2 = list(sentence)
    for x in range(0, len(sentence)):
       #Looping through each letter and changing case. 
        if sentence[x].isupper() == True:
           sentence2[x] = sentence[x].lower()
        elif sentence[x].islower() == True:
            sentence2[x] = sentence[x].upper()
    #Joining the split up leets
   # print(sentence2)
    sentence = ''.join(sentence2)

    #Splitting up indo list of words
    splitSent = sentence.split()

    #Reversing the list
    splitSent.reverse()
    
    #Joining reverse list
    sentence = ' '.join(splitSent)
    print(sentence)

 


reverse_words_order_and_swap_cases("Awesome is Coding")


 