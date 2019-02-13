#!/usr/bin/env python3

# -------------------------------------------------

# Author: Wen Yu (Amy) Wong - wwong3
# Date: 11-FEB-2019
# Purpose: Tic-Tac-Toe Game

# -------------------------------------------------

"""tictactoe"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """get args"""
# Don't include choices within the parser.add arguments or else it will fail make test
# i.e. choices for player as [X, O], will print different error message then expected make test output

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--state', help='Board state',
                        metavar='str', type=str, default='---------')
    parser.add_argument('-p', '--player', help='Player',
                        metavar='str', type=str, default='')
    parser.add_argument('-c', '--cell', help='Cell to apply -p', 
                        metavar='int', type=int)
    return parser.parse_args()



# --------------------------------------------------
def main():
	"""main"""
	args = get_args()
	state_arg = args.state
	player_arg = args.player
	cell_arg = args.cell	

# Determining whether there is a bad state argument
	# counting for -XO
	ok_state={i:0 for i in '-XO'}
	count=0
	for i, letter in enumerate(state_arg):
		if letter in ok_state:
			count +=1

	# Determining coniditions when state dies
	if len(state_arg) !=9 or count !=9:
		print('Invalid state "{}", must be 9 characters of only -, X, O'.format(state_arg))
		sys.exit(1)
						
# Determining whether there is a valid player
	if len(player_arg) !=0:
		if player_arg !='X' and player_arg !='O':
			print('Invalid player "{}", must be X or O'.format(player_arg))
			sys.exit(1)

# Determining whether there is valid cell
	if cell_arg != None:
		if not 0 < cell_arg <10:
			print('Invalid cell "{}", must be 1-9'.format(cell_arg))
			sys.exit(1)


# If --player or --cell is provided, it will error to indicate that both is needed
	if len(player_arg) ==0 and cell_arg !=None or len(player_arg) !=0 and cell_arg ==None:
		if (not player_arg) or (not cell_arg):
			print('Must provide both --player and --cell')
			sys.exit(1)	


	board()


# --------------------------------------------------
def board():
	cell=[1,2,3,4,5,6,7,8,9]
	# assign values to the different cells
	square=['| 1 | 2 | 3 |\n','| 4 | 5 | 6 |\n','| 7 | 8 | 9 |\n']
	
	# print cells as a string type with the border 
	
	print('-------------\n'.join(['']+square+['']))

# --------------------------------------------------
# def bad_state(args):
#	state_arg=args.state	
#	if len(state_arg) != 9:
#		print('"{}" must be 9 characters of only -, X, O'.format(state_arg))
#		sys.exit(1)
#	if state_arg !=state_arg.choices
#		print('"{}" must be 9 characters of only -, X, O'.format(state_arg))
#		sys.exit(1)
# --------------------------------------------------
if __name__ == '__main__':
    main()
