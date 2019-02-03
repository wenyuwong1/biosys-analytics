#!/usr/bin/env python3

# Author: wwong3
# Date: 2019-Jan-29
# Purpose: 03-python Hello Homework


"""hello"""

import os
import sys


def main():
    args = sys.argv[1:]


    if len(args) == 0:
        print ('Usage: {} NAME [NAME...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    elif len(args) == 1:
        print ('Hello to the 1 of you: {}!'.format(sys.argv[1]))
        sys.exit(0)
    elif len(args) == 2:
        names = sys.argv[1:3]
        print ('Hello to the 2 of you: {}!'.format(' and '.join(names)))
        sys.exit(0)
    elif len(args) > 2:
        n = len(args)
        names = args [0: ]
        s_first=", "
        lastname=names.pop()
        x=(s_first.join(names[0:]))
        print ('Hello to the {} of you: {}, and {}!'.format(n, x, lastname))
        sys.exit(0)

main()
