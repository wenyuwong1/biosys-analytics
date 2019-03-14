#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-MAR-14
Purpose: Bottles of beer song
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
	metavar='int',
        type=int,
        default=10)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
	"""Make a jazz noise here"""
	args = get_args()
	bottles = args.num_bottles

	for bottles in range(bottles,0,-1): # -1 decrease by 1 each time 
		if bottles > 2:
			print('{} bottles of beer on the wall,'.format(bottles))
			print('{} bottles of beer,'.format(bottles))
			print('Take one down, pass it around,')
			print('{} bottles of beer on the wall!'.format(bottles-1)+'\n')
		if bottles ==2:
			print('{} bottles of beer on the wall,'.format(bottles))
			print('{} bottles of beer,'.format(bottles))
			print('Take one down, pass it around,')
			print('{} bottle of beer on the wall!'.format(bottles-1)+'\n') # proper grammer for 1 bottle
		if bottles == 1:
			print('{} bottle of beer on the wall,'.format(bottles)) # proper grammer for 1 bottle
			print('{} bottle of beer,'.format(bottles)) # proper grammer for 1 bottle
			print('Take one down, pass it around,')
			print('{} bottles of beer on the wall!'.format(bottles-1)) # 0 bottles is proper grammer
			break





# --------------------------------------------------
if __name__ == '__main__':
    main()
