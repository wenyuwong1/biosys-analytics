#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-FEB-26
Purpose: FASTA GC Segregator
"""

import argparse
import sys
import os
from Bio import SeqIO
from collections import Counter

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FILE', help='Input FASTA file(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        default=50)

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
	fastas = args.fasta
	outdir = args.outdir
	pgc = args.pct_gc

	# If out_dir directory not available, will make the directory
	if not os.path.isdir(outdir):
		os.mkdir(outdir)

	# Determine if pgc value is between 0 and 100 (inclusive)
	if pgc !=None: 
		if not 1<= pgc <=100:
			print('--pct_gc "{}" must be between 0 and 100'.format(pgc))
			exit(1)

        # Determine if fasta value is a file
	num_seqs=0 # Will count num of seq sorted for later
	for i,  file in enumerate(fastas): # Use enumerate so you can print the num: file
		if not os.path.isfile(file):
			warn('"{}" is not a file'.format(file))
			continue
		else:
			basename, ext = os.path.splitext(os.path.basename(file)) # Split basename
			high_file=os.path.join(outdir,basename+'_high'+ext) # Creating place for high GC
			low_file=os.path.join(outdir,basename+'_low'+ext) # Creating place for low GC

			high_file_fh=open(high_file, 'wt') # file handle for High GC
			low_file_fh=open(low_file, 'wt') # file handle for Low GC

			for record in SeqIO.parse(file, 'fasta'): # parsing file
				num_seqs+=1 # counting num of seq
				seq_len=len(record.seq) # count num of NT
				nucs=Counter(record.seq)
				gc_num=nucs.get('G', 0)+nucs.get('C', 0) #get G and C safely
				gc=(gc_num/seq_len)*100 # calc percentage

				if gc < pgc:
					SeqIO.write(record, low_file_fh, 'fasta')
				else:
					SeqIO.write(record, high_file_fh, 'fasta')
		num_file=len(fastas)
		print('{}: {}'.format(i+1, os.path.basename(file)))
	print('Done, wrote {} sequences to out dir "{}"'.format (num_seqs, outdir))


						
# --------------------------------------------------
if __name__ == '__main__':
    main()
