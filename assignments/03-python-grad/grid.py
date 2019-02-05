#!/usr/bin/env python3

# Author: wwong3
# Date: 2019-Jan-31
# Purpose: 03-python Grad Grid Homework


"""grid"""

import os
import sys

def main():
    num = sys.argv[1:]
   

# Error message with usage
    if len(num) == 0:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

# Error message if more than one arguments
    if len(num)>1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1) 

# First if statement: Error if num is not between 2 and 9
# Elif statement: If num is between 2 and 9, will display grid 
    num=int(num[0]) #changes num from a list to an integer
    if  not 2<= num <10:
        print('NUM ({}) must be between 1 and 9'.format(num))
        sys.exit(1)
    elif 1 < num < 10:
        last_num=num+1 # to include last number through indexing
        for j in range (1,last_num): # iterate through cols
            for i in range(1,last_num): # iterate through rows         
                print('{:>3d}'.format(i+num*(j-1)),end='')
                # i+num*(j-1) is pattern for grid output
                # don't use {:>2d) with end=' ' > will give you extra space at end of line
                #{:>3d} is string formatting
                 # 3=num of character field, d=decimal, > means right-aligned
            print('') #print new line
          
        exit(0)
main()
