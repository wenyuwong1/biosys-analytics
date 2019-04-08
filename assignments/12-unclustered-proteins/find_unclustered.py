#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-April-04
Purpose: Unclustered Proteins
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered protein)',
        metavar='str',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')	

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
	cdhit=args.cdhit
	proteins=args.proteins
	outfile=args.outfile

	if not os.path.isfile(proteins):
		die('--proteins "{}" is not a file'.format(proteins))
	if not os.path.isfile(cdhit):
		die('--cdhit "{}" is not a file'.format(cdhit))

		


# --------------------------------------------------
if __name__ == '__main__':
    main()
