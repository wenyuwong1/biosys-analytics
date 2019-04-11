#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file = args[0]
if not os.path.isfile(file):
    print('"{}" is not a file'.format(file))
    sys.exit(1)

def wordnum(word):
    return str(sum(map(ord, word)))

for line in open(file):
    words = line.rstrip().split()
    nums = map(wordnum, words)
    print(' '.join(nums))

