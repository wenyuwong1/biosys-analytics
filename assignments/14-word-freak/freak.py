#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-April-19
Purpose: Word count
"""

import argparse
import sys
import os
import re
from collections import Counter
from re import split

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Sorting by word or frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='File input(s)', nargs='+')

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)

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
def word_count(file,counter):
	#counter=Counter()
	with open(file, 'r') as fh:
		line=fh.read().rstrip().lower().split()
		word_list=[]
		for word in line:
			word_list.append(re.sub('[^a-zA-Z0-9]', '', word))
		word_list=list(filter(None, word_list)) #removes empty string from word_list
		counter.update(word_list)
	return counter

# --------------------------------------------------
def main():
	"""Make a jazz noise here"""
	args = get_args()
	files = args.files
	sorto = args.sort
	mini = args.min
	
	lst = Counter()
	for file in files:
		lst=word_count(file,lst)

	if "frequency" in sorto:
		pairs = sorted([(x[1], x[0]) for x in lst.items()])
		for count, word in sorted(pairs):
			if mini!=None:
				if count >= mini:
					print('{:20} {}'.format(word, count))
	elif "word" in sorto:
		for word, count in sorted(lst.items()):
			if mini!=None:
				if count >= mini:
					print('{:20} {}'.format(word, count))

# --------------------------------------------------
if __name__ == '__main__':
    main()
