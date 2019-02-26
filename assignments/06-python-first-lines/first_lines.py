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
        'directories', metavar='DIR', help='Directory name', nargs='+')

    parser.add_argument(
        '-w',
        help='width',
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
	dirs=args.directories
	width=args.w
	
	# Determine if positional value is a directory
	for dir in dirs:
		if not os.path.isdir(dir):
			print('"{}" is not a directory'.format(dir), file=sys.stderr)
			continue
		dir_dict={} # create empty to store keys and f_line later
		print(dir)
		files = os.listdir(dir)
		for file in files:
			path=os.path.join(dir,file) # path relative to script location
			with open(path) as f:
				f_line=f.readline().rstrip() # read first line and strip /n
				dir_dict[f_line]=file
		dir_sort=sorted(dir_dict.keys())
		for f_line in dir_sort:
			file=dir_dict[f_line]
			dots='.'*(width-len(f_line)-len(file)) # figure out num of dots needed
			print('{} {} {}'.format(f_line, dots, dir_dict[f_line])) 



# --------------------------------------------------
if __name__ == '__main__':
	main()
