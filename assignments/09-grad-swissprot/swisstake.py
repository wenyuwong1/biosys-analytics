#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-MAR-14
Purpose: Parsing SwissProt
"""

import argparse
import sys
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
	"""get command-line arguments"""
	parser = argparse.ArgumentParser(description='Filter Swissprot file for keywords, taxa',formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('file', metavar='FILE', help='Uniprot file')

	parser.add_argument(
		'-s',
		'--skip',
		help='Skip taxa',
		metavar='STR',
		type=str,
		default='',
		nargs='+')

	parser.add_argument(
		'-k',
		'--keyword',
		help='Take on keyword',
		metavar='STR',
		type=str,
		default=None,
		required=True)

	parser.add_argument(
		'-o',
		'--output',
		help='Output filename',
		metavar='FILE',
		type=str,
		default='out.fa')


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
	file=args.file
	keyword=args.keyword
	keyword=set([keyword]) # Do Not lower or upper case...this is not case-insensitive
	skip=args.skip
	skip=set([s.lower() for s in skip]) # Setting these variables make it easier to use intersect later
	outfile=args.output


	if not os.path.isfile(file):
		die('"{}" is not a file'.format(file))

	# If file and keyword given
	out_fh=open(outfile, 'wt')
	
	print('Processing "{}"'.format(file))

	num_skips=0
	num_found=0

	for record in SeqIO.parse(file, "swiss"):
		annotations=record.annotations 
		if 'keywords' in annotations: # search specifically for the value=keywords in annotations
			word_list=set([w.lower() for w in annotations['keywords']]) # extract out keywords from annotations and set
			taxa_list=set([t.lower() for t in annotations['taxonomy']]) # extract out taxonomy from annotations and set

			if keyword.intersection(word_list) and not skip.intersection(taxa_list): # intersection finds values in both lists
				num_found+=1
				SeqIO.write(record, out_fh, 'fasta')
			else:
				num_skips+=1
	# Print('I give up')	
	print('Done, skipped {} and took {}. See output in "{}".'.format(num_skips, num_found, outfile))
	

	

# --------------------------------------------------
if __name__ == '__main__':
    main()
