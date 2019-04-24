#!/usr/bin/env python3
"""tests for makingmoney.py"""

from subprocess import getstatusoutput, getoutput
import argparse
import sys
import os
import re
import string
import random
import datetime,time
import makingmoney

prg = "./makingmoney.py"


# -------------------------------------------------
def random_num():
    """generate a random time"""
    return ''.join(random.choices(string.digits+'[:]'+string.digits, k=1))

# --------------------------------------------------
def test_usage():
    """usage"""
    rv1, out1 = getstatusoutput(prg)
    assert rv1 > 0
    assert re.match("usage", out1, re.IGNORECASE)

# --------------------------------------------------
def test_bad_input():
    """bad_input"""
    bad_time = random_num()
    rv, out = getstatusoutput('{} {} {}'.format(prg, bad_time, bad_time))
    assert rv >= 0
    assert re.search("error", out, re.IGNORECASE)

# --------------------------------------------------
def test_ok1():
    """makingmoney ok1"""
    expected1="You started at 09:00:00 and ended at 13:00:00\nYou worked for 4:00:00 hours\nYou earned $32.00"
    tests = [('09:00', '13:00')]

    for s, e in tests:
        rv, out=getstatusoutput('{} -s {} -e {}'.format(prg, s, e))
        assert rv ==0
    assert out == expected1


# --------------------------------------------------
def test_ok2():
    """makingmoney ok2"""
    expected2="You started at 08:31:00 and ended at 14:00:00\nYou worked for 5:29:00 hours\nYou earned $43.87"
    tests = [('08:31', '14:00')]

    for s, e in tests:
        rv, out=getstatusoutput('{} -s {} -e {}'.format(prg, s, e))
        assert rv ==0
    assert out == expected2


# --------------------------------------------------
