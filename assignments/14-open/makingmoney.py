#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-04-22
Purpose: Rock the Casbah
"""

import argparse
import sys
import datetime,time

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Making Money script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--start',
	help='Military Time-In',
	required=True,
        metavar='HH:MM',
        type=datetime.time.fromisoformat)

    parser.add_argument(
        '-e',
        '--end',
        help='Military Time-Out',
        required=True,
        metavar='HH:MM',
        type=datetime.time.fromisoformat)

    parser.add_argument(
        '-w',
        '--wage',
        help='The wage a person earns (ie: 9.25)',
        metavar='float',
        type=float,
        default=8.0)

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
	start = str(args.start)
	end = str(args.end)
	wage = args.wage


        # convert user input to datetime instances
	start_t=datetime.time(hour=int(start[0:2]), minute=int(start[3:5]))
	end_t = datetime.time(hour=int(end[0:2]), minute=int(end[3:5]))
	delta_t = datetime.timedelta(
                hours = (end_t.hour - start_t.hour),minutes = (end_t.minute - start_t.minute))

	hours=(delta_t.seconds/3600)

        # calculating wage
	amt = hours* wage

        # output
	print('You started at {} and ended at {}'.format(start_t, end_t))
	print('You worked for {} hours'.format(delta_t))
	print('You earned ${0:.2f}'.format(round(amt, 2)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
