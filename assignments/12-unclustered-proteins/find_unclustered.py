#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-April-04
Purpose: Unclustered Proteins
"""

import argparse
import sys
import os
import re
from Bio import SeqIO

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
    cdhit = args.cdhit
    proteins = args.proteins
    outfile = args.outfile

    if not os.path.isfile(proteins):
        die('--proteins "{}" is not a file'.format(proteins))
    if not os.path.isfile(cdhit):
        die('--cdhit "{}" is not a file'.format(cdhit))

    cdhit_match = re.compile('(>gi)'
                             '[|]'
                             '(?P<PID>\d+)'
                             '[|]')

    clustered = set()

    with open(cdhit) as hit_handle:
        for line in hit_handle:
            m1 = cdhit_match.search(line)
            if m1==None:
                continue
            clustered.add(m1.group('PID'))

    unclustered = 0
    num_proteins = 0

    out_file=open(outfile, 'wt')
    with open(proteins) as protein_handle:
        for record in SeqIO.parse(protein_handle, 'fasta'):
            num_proteins+=1
            m2=re.search('(?P<ID>\d+)', record.id) #record.id drops the >
            if m2==None:
                continue
            ID=m2.group('ID')

            if ID not in clustered:
                unclustered+=1
                SeqIO.write(record, out_file, "fasta")
    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(unclustered, num_proteins, outfile))




# --------------------------------------------------
if __name__ == '__main__':
    main()
