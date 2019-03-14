#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-FEB-27
Purpose: CSV parsing on genus and species
"""

import argparse
import sys
import os
import csv

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'blast', metavar='FILE', help='BLAST output')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')


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
	blasts = args.blast
	annot = args.annotations
	outfile = args.outfile

	# Check if annot and blasts are files
	for files in [blasts, annot]:
		if not os.path.isfile(files):
			die('"{}" is not a file'.format(files))

	# adding headers to annotation files
	species={}
	genus={}

	with open(annot) as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			if not row['genus']=='':
				genus[row['centroid']]=row['genus']
			else:
				genus[row['centroid']]='NA' #setting to NA if there's an empty string
			if not row['species']=='':
				species[row['centroid']]=row['species']
			else:
				species[row['centroid']]='NA'

	# Setting up the outfile, open here and adding the headers here
	out_fh=open(outfile, 'wt') if outfile else sys.stdout
	headers=("seq_id", "pident", "genus", "species")
	out_fh.write('\t'.join(headers)+'\n')
	
	with open(blasts) as csvfile:
		reader=csv.DictReader(csvfile, delimiter='\t', fieldnames=('qaccver', 'saccver', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'))
		for row in reader:
			seq_id=row['saccver']
			pident=row['pident']
			if not seq_id in genus:
				warn('Cannot find "{}" in lookup'.format(seq_id))
			else:
				# Need to call genus[seq_id] so you can match correct ones
				out_fh.write(seq_id+'\t'+pident+'\t'+genus[seq_id]+'\t'+species[seq_id]+'\n')
				
 

# --------------------------------------------------
if __name__ == '__main__':
    main()
