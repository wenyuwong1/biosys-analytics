#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-MAR-26
Purpose: Regular Expression Data Parsing
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
   
    input_date=sys.argv[1]

    date_re1=re.compile('(?P<year>\d{4})'
                        '([/-])?'
                        '(?P<month>\d{,2})'
                        '([/-]?)'
                        '(?P<day>\d{,2}?)'
                        '($|[A-Z].*|/)')

    date_re2=re.compile('(?P<month>\d{1,2})'
                        '([/-])'
                        '(?P<year>\d{,2})')

    date_re3=re.compile('(?P<month>\D+)'
                        '([\s,-]+)'
                        '(?P<year>\d{,4})')


    date1=date_re1.match(input_date)
    date2=date_re2.match(input_date)
    input_date=input_date.lower()
    date3=date_re3.match(input_date)

    mth = {
        'jan' :'01',
        'feb' :'02',
        'mar' :'03',
        'apr' :'04',
        'may' :'05',
        'jun' :'06',
        'jul' :'07',
        'aug' :'08',
        'sep' :'09',
        'oct' :'10',
        'nov' :'11',
        'dec' :'12'}

    if date1:
        year=date1.group('year')
        month=date1.group('month')
        if len(month)<2:
           month='0'+month
        day=date1.group('day')
        if len(day)==0:
           day='01'
        if len(day)==1:
           day='0'+day
        print('{}-{}-{}'.format(year, month, day))
    elif date2:
        year=date2.group('year')
        if len(year)<4:
           year='20'+year   
        month=date2.group('month')
        if len(month)<2:
           month='0'+month
        print('{}-{}-{}'.format(year, month, '01'))
    elif date3:
        year=date3.group('year')
        month=date3.group('month')
        month=mth.get(month[0:3])
        print('{}-{}-{}'.format(year, month, '01'))
    else:
        print('No match')


# --------------------------------------------------
main()
