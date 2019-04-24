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
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='Input files', nargs=2)

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
	return diffs+len_diff

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
	
# --------------------------------------------------
def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]

# -------------------------------------------------
def common(words1, words2, distance):
	final=list(zip(words1, word2, distance))
	return final 
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
		filename='.log',
		filemode='w',
		level=logging.DEBUG if args.debug else logging.CRITICAL)


	for fname in files:
		if not os.path.isfile(fname):
			die(msg='"{}" is not a file'.format(fname))


	logging.debug('file1={}, file2={}'.format(files[0], files[1]))

	if distance < 0:
		print('--distance "{}" must be > 0'.format(distance))
		exit(1)


	word1=[]
	word2=[]
	with open(files[0]) as fh1:
		word1=[word for line in fh1 for word in line.split()]

	with open(files[1]) as fh2:
		word2=[word for line in fh2 for word in line.split()]

	w1=word1
	w2=word2
	
	combo=list(zip(word1, word2))
	hamm=[]
	for word1, word2 in combo:
		d=dist(word1, word2)
		hamm.append(d)
		logging.debug(msg='s1= {}, s2= {}, d= {}'.format(word1, word2, d))

	final=list(zip(w1, w2, hamm))

	for w1, w2, hamm in final:
		print('{}\t{}\t{}'.format(w1, w2, hamm))


# --------------------------------------------------
if __name__ == '__main__':
    main()
