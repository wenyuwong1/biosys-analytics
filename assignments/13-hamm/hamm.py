#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-04-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import logging

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
	# need this is one word is longer than the other
	len_diff=abs(len(s1)-len(s2))
	for chr1, chr2 in zip(s1, s2):
		if chr1 != chr2:
			diffs+=1
	return diffs+len_diff
	

# --------------------------------------------------
def main():
	"""Make a jazz noise here"""
	args = get_args()
	files=args.file

	logging.basicConfig(
		filename='.log',
		filemode='w',
		level=logging.DEBUG if args.debug else logging.CRITICAL)
	
	for txt in files:
		if not os.path.isfile(txt):
			die(msg='"{}" is not a file'.format(txt))

	
	logging.debug('file1={}, file2={}'.format(files[0], files[1]))

# Can't use below because spaces screw up hamming distance, wonder if you could do it to skip space
#	str1=''
#	str2=''
#	with open(files[0]) as fh1:
#		str1=fh1.read().replace('\n', '')
#
#	with open(files[1]) as fh2:
#		str2=fh2.read().replace('\n', '')

#	print(str1)
#	print(str2)

	word1=[]
	word2=[]
	with open(files[0]) as fh1:
		word1=[word for line in fh1 for word in line.split()]

	with open(files[1]) as fh2:
		word2=[word for line in fh2 for word in line.split()]
	
	combo=list(zip(word1, word2))
	hamm=0
	for word1, word2 in combo:
		d=dist(word1, word2)
		logging.debug('s1={}, s2={}, d={}'.format(word1, word2, d))
		hamm+=d
	print(hamm)

# --------------------------------------------------
	


# --------------------------------------------------
if __name__ == '__main__':
    main()
