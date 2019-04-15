#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-04-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamm Distance Script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='FILE',type=str, help='File inputs', nargs=2)

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true', default=False)

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
def dist(s1, s2):	
	diffs=0
	for chr1, chr2 in zip(s1, s2):
		if chr1 != chr2:
			diffs+=1
	return diffs
	

# --------------------------------------------------
def main():
	"""Make a jazz noise here"""
	args = get_args()
	files=args.file
	debug = args.debug

	for txt in files:
		if not os.path.isfile(txt):
			die(msg='"{}" is not a file'.format(txt))

	word1=[]
	word2=[]

	with open(files[0]) as fh1:
		word1=([word for line in fh1 for word in line.split()])
	
	with open(files[1]) as fh2:
		word2=([word for line in fh2 for word in line.split()])
	
	dist(word1, word2)

# --------------------------------------------------
	


# --------------------------------------------------
if __name__ == '__main__':
    main()
