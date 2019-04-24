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
import tabulate

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

	if distance <= 0:
		print('--distance "{}" must be > 0'.format(distance))
		exit(1)

# --------------------------------------------------
if __name__ == '__main__':
    main()
