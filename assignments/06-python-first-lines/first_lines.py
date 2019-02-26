#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-FEB-20
Purpose: Prints the first line of the contents of each file in a directory
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='First Line Script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DIR', help='Directory name', nargs='+')

    parser.add_argument(
        '-w',
        help='width',
        metavar='int',
        type=int)

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
	dir=args.positional
	width=args.w

	# Error msg if input is not a directory
	dir.verifyIsDirectory()
	print('{} is not a file'.format(dir))
	exit(1)
	


# --------------------------------------------------
if __name__ == '__main__':
    main()