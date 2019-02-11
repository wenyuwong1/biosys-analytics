#!/usr/bin/env python3

# Author: wwong3
# Date: 05-FEB-2019
# Purpase: 04 Python homework, read the lines in a file via python


# ---------------------------------
"""cat_n.py"""

import os
import sys

# ---------------------------------

args = sys.argv[1:]

# Print error message if there are no arguments
if len(args) != 1:
	print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

# Print error message if the argument is not a file
file=args[0]
if not os.path.isfile(file):
	print('{} is not a file'.format(file))
	sys.exit(1)

#-------------------------------------

def main():
	
	if len(args)==1:
		f=open(file)
		for i, line in enumerate(f):
			print('{:>3}: {}'.format(i+1, line), end='')
	sys.exit(0)
main()
 


