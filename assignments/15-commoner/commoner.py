#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-April-23
Purpose: Find Common Words with Mismatch
"""

import argparse
import sys
import os
import logging
import io
import re
from itertools import product
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='Input files', nargs=2, type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument(
        '-d',
        '--debug',
        help='Debug',
        action='store_true',
        default=False)

    parser.add_argument(
        '-t',
        '--table',
        help='Table output',
        action='store_true',
        default=False)

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
	d=diffs+len_diff

	logging.debug('s1={}, s2={}, d={}'.format(s1, s2, d))

	return d

# --------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n
# --------------------------------------------------
def uniq_words(file, min_len):
	"""find unique words in a file """
	words=set()	
	for line in file:
		for word in line.lower().split():
			good=(re.sub('[^a-zA-Z0-9]', '', word))
			if len(good)==0:
				continue
			if len(good)>=min_len:
				words.add(good)

	logging.debug('{}'.format(words))

	return words

# --------------------------------------------------
def common(words1, words2, distance):
	same=list()
	for w1, w2 in sorted(product(words1, words2)):
		dis=dist(w1, w2)
		if dis<=distance:
			lst=(w1, w2, dis)
			same.append(lst)
	return same

# -------------------------------------------------
def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]

# --------------------------------------------------
def main():
	"""Make a jazz noise here"""
	args = get_args()
	files = args.files
	mini = args.min_len
	distance = args.hamming_distance
	logfile = args.logfile
	debug = args.debug
	table = args.table

	logging.basicConfig(
		filename=logfile,
		filemode='w',
		level=logging.DEBUG if args.debug else logging.CRITICAL)

	logging.debug('file1={}, file2={}'.format(files[0], files[1]))

	if distance < 0:
		die('--distance "{}" must be > 0'.format(distance))

	words1=uniq_words(files[0], mini)
	words2=uniq_words(files[1], mini)
	final=common(words1, words2, distance)

	final.sort()
	if final:
		if table:
			print(tabulate(final, headers=["word1", "word2", "distance"], tablefmt="psql"))
		else:
			print('{}\t{}\t{}'.format('word1', 'word2', 'distance'))
			for lst in final:
				print('{}\t{}\t{}'.format(lst[0], lst[1], lst[2]))
	else:
		print('No words in common.')

	

# --------------------------------------------------
if __name__ == '__main__':
    main()
