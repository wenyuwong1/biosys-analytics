#!/usr/bin/env python3

# Author: wwong3 (Wen Yu Amy Wong)
# Date: 2019-Jan-31
# Purpose: 03-python Vowel_Counter Homework 

"""vowel_counter"""

import os
import sys

def main():
    args = sys.argv[1:]
    word=args

    if len(word) == 0:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    elif len(word) != 0:
        word=str(word[0])          ### Used to set the argument word to a string instead of a list
        def vowel_count(word):
            count=0
            vowels ="aeiouAEIOU"
            for i in word:
                if i in vowels:
                    count=count +1 
            if count == 0:      
                print('There are 0 vowels in "{}."'.format(word))
            elif count == 1:
                print('There is 1 vowel in "{}."'.format(word))
            elif count > 1:
                n=count
                print('There are {} vowels in "{}."'.format(n,word))     
        vowel_count(word)
main()
         
