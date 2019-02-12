#!/usr/bin/env python3

# Author: wwong3
# Date: 05-FEB-2019
# Purpose: 04 Python homework, function like head command


# ---------------------------------
"""head.py"""

import os
import sys

# ---------------------------------

args = sys.argv[1:]

# Print error and usage statement if more there is 0  arg
if len(args) ==0:
        print('Usage: {} FILE [NUM_LINE]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

# Print error and usage statement if more than 2 arg
if len(args) >2:
        print('Usage: {} FILE [NUM_LINE]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

# Print error message if the first argument is not a file
file=args[0]
if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

# Print error message if the second argument is not a positive number
if len(args) >1:
	if int(args[1])<=0:
		print('lines ({}) must be a positive number'.format(args[1]))
		sys.exit(1)

#-------------------------------------
if len(args)==1:
	num_lines=3
else:
	num_lines=args[1]

def main(file=file, num_lines=num_lines):
	i=0
	with open(file) as f:
		for line in f.readlines():
			if i < int(num_lines):
				i+=1
				print('{}'.format(line), end='')
			else:
				break
main()

#-----------------------------------

