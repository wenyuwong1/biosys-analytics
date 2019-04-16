#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-04-15
Purpose: De Bruijn Graphs in Python
"""

import argparse
import sys
import os
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Graph through sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='str', help='FASTA file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='K size of overlap',
        metavar='int',
        type=int,
        default=3)

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
def find_kmers(string, k):
	n=len(string)-k+1
	found=[]	

	for i in range(0,n,1):
		found.append(str(string[i:i+k]))
	return found

# --------------------------------------------------
def main():
	"""Make a jazz noise here"""
	args = get_args()
	k = args.overlap
	fasta = args.fasta

	if not os.path.isfile(fasta):
		die(msg='"{}" is not a file'.format(fasta))

	if k<=0:
		die(msg='-k "{}" must be a positive integer'.format(k))

	kmers_begin={}
	kmers_end={}
	for record in SeqIO.parse(fasta, 'fasta'):
		seq_k=find_kmers(record.seq,k)
		kmers_begin[record.id]=(seq_k[0])
		kmers_end[seq_k[-1]]=record.id
	
	for key, value in kmers_begin.items():
		if value in kmers_end.keys():
			if kmers_end.get(value) != key:
				print(kmers_end.get(value), key)
			

#	for kmer in kmers_begin.values():
#		print(kmer)
#		if kmer in kmers_end.values():
#			print('yes')		

# --------------------------------------------------
if __name__ == '__main__':
    main()
