#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-April-02
Purpose: Password Parsing
"""

import os
import sys
import re

# --------------------------------------------------
def main():
 
    args = sys.argv[1:]

    if len(args) !=2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    pw=args[0]
    alt=args[1]

    alt1=pw.upper()
    alt2=pw[0].upper()+pw[1:]

    addition_char=re.compile('.?'+pw+'.?')

    if pw==alt:
        print('ok')
    elif alt==alt1:
        print('ok')
    elif alt==alt2:
        print('ok')
    elif addition_char.match(alt):
        print('ok')
    else:
        print('nah')
    


# --------------------------------------------------
main()
