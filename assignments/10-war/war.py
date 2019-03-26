#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-MAR-19
Purpose: War Game >.<
"""

import argparse
import sys
import random
from itertools import product

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='War Games!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Seed Thingy for Random Generator',
        metavar='int',
        type=int,
        default=None)

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
	seed = args.seed

	if seed is not None:
		random.seed(seed)
	
	suits=['♥', '♠', '♣', '♦']
	num=['2','3','4','5','6','7','8','9','10','J','Q','K','A']	
	combo_cards=list(product(suits,num))
	
	# Create combo for cards with suites and value	
	deck=[]
	for combo in combo_cards:
		card=''.join(combo)
		deck.append(card)
	
	deck.sort()
		
	
	random.shuffle(deck)

	P1_wins=0
	P2_wins=0
	#P1=[]
	#P2=[]
	
	# Pop off each card to each player
	#while len(deck)>0:
	#	P1.append(deck.pop())
	#	P2.append(deck.pop())

	while deck:
		Player1_card=deck.pop()
		Player2_card=deck.pop()
		P1_value=num.index(Player1_card[1:])
		P2_value=num.index(Player2_card[1:])
				
		if P1_value > P2_value:
			P1_wins+=1
			winner='P1'
		elif P2_value > P1_value:
			P2_wins+=1
			winner='P2'
		else:
			winner='WAR!'
		print('{:>3} {:>3} {}'.format(Player1_card, Player2_card, winner))
		#if len(P1)==0:
		#	break
	if P1_wins > P2_wins:
		won='Player 1 wins'
	elif P2_wins > P1_wins:
		won='Player 2 wins'
	else:
		won='DRAW'
	print('P1 {} P2 {}: {}'.format(P1_wins, P2_wins,won)) 
		


	

# --------------------------------------------------
if __name__ == '__main__':
    main()
