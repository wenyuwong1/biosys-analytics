#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-04-22
Purpose: Converting User Time Inputs and Calculate Hourly Wage
"""

import os
import sys
import datetime, time

# --------------------------------------------------
def main():
	start = input("Enter your time-in time in military format (0900): ") 
	end = input("Enter your time-out time in military format (1700): ") 

	if len(start)<4 or len(end)<4:
		print('Error: Enter time-in with 4 digits in military format')
		sys.exit(1)

	wage = int(float(input("Enter you hourly wage (8.00): ")))

	# convert user input to datetime instances
	start_t = datetime.time(hour=int(start[0:2]), minute=int(start[2:4]))
	end_t = datetime.time(hour=int(end[0:2]), minute=int(end[2:4]))
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
main()
