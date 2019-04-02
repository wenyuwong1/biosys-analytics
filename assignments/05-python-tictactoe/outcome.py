#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-FEB-17
Purpose: Win conditions for Tic-Tac-Toe
"""

import os
import sys


# --------------------------------------------------
def main():
        args = sys.argv[1:]


        # If there is not exactly 1 argument, print usage statement
        if len(args) != 1:
                print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
                exit(1)


        # Determine that the STATE argument must be 9 characters and only contain .,X,O
        STATE= args[0] # Setting STATE = args[0]
        # count for .XO
        count=0
        for char in STATE:
                if char in "XO.":
                        count+=1

        # Dies if STATE isn't 9 characters and contain other char than .XO
        if len(STATE) !=9 or count !=9:
                print('State "{}" must be 9 characters of only ., X, O'.format(STATE))
                exit(1)

        # Determine win vs non-win conditions based on STATE

        # Check for win states
        win=[(0,1,2),
         (3,4,5),
         (6,7,8),
         (0,3,6),
         (1,4,7),
         (2,5,8),
         (0,4,8),
         (2,4,6)]

        # For loop through the different win conditions to check for wins
        for conditions in win:
                if all(STATE[i]=='X' for i in conditions):
                        print('X has won')
                        break
                elif all (STATE[i]=='O' for i in conditions):
                        print('O has won')
                        break
        else:
             	print('No winner')

# --------------------------------------------------
main()
