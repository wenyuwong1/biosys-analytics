#!/usr/bin/env python3
"""
Author : Wen Yu (Amy) Wong- wwong3
Date   : 2019-FEB-14
Purpose: Translate Codons to Proteins
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
	'-c',
	'--codons',
	help='A file with codon translations',
	metavar='FILE',
	type=str,
	required=True,
	default=None)

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

  
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
	STR = args.positional
	codon = args.codons
	output = args.output

# Die and exit when bad --codons are given or when codon is not a file
	if not os.path.isfile(codon):
		print('--codons "{}" is not a file'.format(codon))
		exit(1)

# If given good input, write results in proper output file:
	
	# Taking string and upper case them
	STR=STR.upper()
		
	# Splitting --codon into 3 characters and storing into var=STR
	n=3
	STR=[STR[i:i+3] for i in range(0,len(STR), n)] 

	# Splitting --codon file so you can associate sequence to protein
	codon_dict={} # empty directory
	for line in open (codon): # reading in line of the --codon file
		codon,amino_acid=line.split() # split on white space, rename pieces
		codon_dict[codon]=amino_acid # renaming 
		
	# Matching each codon STR to --codon FILE

	protein_list='' # Creating new empty str to later store all the codon matches
	for i in STR: # Calling each index in STR list
		if i in codon_dict: # Passing those index into the codon_dict 
			protein=codon_dict[i] # Finding the protein matches
		else:
			protein='-'
	
		protein_list += protein # Adds the found protein to the protein_list

	# Creating store lists to correct output file
	with open (output, "wt") as outgoing: # Opening output file and "wt"=writing
		print(protein_list, file=outgoing) # Telling it to add the protein_list to file
		print('Output written to "{}"'.format(output)) # Msg, output file is written
		

# --------------------------------------------------
if __name__ == '__main__':
    main()
