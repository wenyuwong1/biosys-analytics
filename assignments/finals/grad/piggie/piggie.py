#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import os.path
import string
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='File input(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='str',
        type=str,
        nargs='+',
        default='out-yay')

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
    files = args.files
    outdir = args.outdir

    if not os.path.isdir(outdir):
        os.mkdir(outdir)

    read=0
    for i, file in enumerate(files):
        if not os.path.isfile(file):
            warn('"{}" is not a file.'.format(os.path.basename(file)))
            continue
        else:
            save_path = outdir
            basename = os.path.basename(file)
            newName = os.path.join(save_path, basename)
            
            out_dir = open(newName, 'w+')
            with open(file, 'r') as fh:
                read+=1
                lines = fh.read().splitlines()
                word_list=[]
                for line in lines:
                    for word in line.split():
                        clean = re.sub('[^a-zA-Z0-9]', '', word)
                        consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
                        match = re.match('^([' + consonants + ']+)(.+)', clean)
                        if match:
                            out_dir.write('-'.join([match.group(2), match.group(1) + 'ay']) + ' ')
                        else:
                            out_dir.write(word + '-yay' +' ')
                    out_dir.write('\n')

    if read == 0:
        print('Done, wrote 0 files to "{}".'.format(outdir))
    elif read ==1:
        print('Done, wrote 1 file to "{}".'.format(outdir))
    else:
        print('Done, wrote {} files to "{}".'.format(read, outdir))


# --------------------------------------------------
if __name__ == '__main__':
    main()
