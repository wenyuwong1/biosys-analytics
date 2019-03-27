#!/usr/bin/env python3
"""
Author : wwong3
Date   : 2019-MAR-26
Purpose: Playing Blackjack
"""

import argparse
import sys
import random
from itertools import product


# --------------------------------------------------
def get_args():
	"""get command-line arguments"""
	parser = argparse.ArgumentParser(
		description='Blackjack game',
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)


	parser.add_argument(
		'-s',
		'--seed',
		help='Seedy Thingy for Random Generator',
		metavar='int',
		type=int,
		default=None)

	parser.add_argument(
        	'-p',
        	'--player_hits',
        	help='Player hits boolean',
        	action='store_true')

	parser.add_argument(
		'-d', 
		'--dealer_hits',
		help='Dealer hits boolean',
		action='store_true')

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
	phits = args.player_hits
	dhits = args.dealer_hits
	
	if seed is not None:
		random.seed(seed)

	suits=['♥', '♠', '♣', '♦']
	num=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	
	# Assign values to cards
	value={}
	for i, rank in enumerate(num, 1):
		if i<=10:
			value[rank]=i
		else:
			value[rank]=10
	
	combo_cards=list(product(suits, num))
	
	
	deck=[]
	for combo in combo_cards:
		card=''.join(combo)
		deck.append(card)
	deck.sort()
	random.shuffle(deck)

	P_card1=deck.pop()
	D_card1=deck.pop()
	P_card2=deck.pop()
	D_card2=deck.pop()
		
	P_card1value=value[P_card1[1:]]
	P_card2value=value[P_card2[1:]]
	D_card1value=value[D_card1[1:]]
	D_card2value=value[D_card2[1:]]

	P_total=P_card1value+P_card2value
	D_total=D_card1value+D_card2value

	P_cards=[P_card1, P_card2]
	D_cards=[D_card1, D_card2]

	if phits:
		P_hits_card=deck.pop()		
		P_hits_value=value[P_hits_card[1:]]
		P_total+=P_hits_value
		P_cards.append(P_hits_card)		

	if dhits:
		D_hits_card=deck.pop()
		D_hits_value=value[D_hits_card[1:]]
		D_total+=D_hits_value	
		D_cards.append(D_hits_card)	
	

	print('D [{:>2}]: {}'.format(D_total, ' '.join(D_cards)))
	print('P [{:>2}]: {}'.format(P_total, ' '.join(P_cards)))
	
	if P_total>21:
		print('Player busts! You lose, loser!')
		exit(0)
	if D_total>21:
		print('Dealer busts.')
		exit(0)
	if P_total==21:
		print('Player wins. You probably cheated.')
		exit(0)
	if D_total==21:
		print('Dealer wins!')
		exit(0)
	if D_total<18:
		print('Dealer should hit.')
	if P_total<18:
		print('Player should hit.')
				


# --------------------------------------------------
if __name__ == '__main__':
    main()
