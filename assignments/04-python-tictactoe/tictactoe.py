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

	# Converting '.' input to '-' output for good state, mutate state and other mutate state 
	state_arg=state_arg.replace('.', '-')

# Determining whether there is a bad state argument
	# counting for -XO
	ok_state={i:0 for i in '-XO'}
	count=0
	for i, letter in enumerate(state_arg):
		if letter in ok_state:
			count +=1

	# Determining coniditions when state dies
	if len(state_arg) !=9 or count !=9:
		state_arg=state_arg.replace('-', '.') # Switching back from - to . so print works
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
	
# From a given state, change one cell to the player's choice
	if len (player_arg) !=0 and cell_arg !=None:
		state_list=list(state_arg) # Changing state_arg into a list
		if state_list[cell_arg-1] in 'XO': # Calling for cell_arg-1 that might have 'XO'
			print('Cell {} already taken'.format(cell_arg))
			sys.exit(1)
		else:
			state_list[cell_arg-1]=player_arg # Setting the cell to the player's choice
			new_state=(''.join(state_list))  # Joining together new state_list
			state_arg=new_state # Updating state_arg to the new inputs 
 

	board(state_arg) # Calling in the new status of state_arg


# --------------------------------------------------
def board(cell):
	new_board=[]
	for i, char in enumerate(cell):
		if char == '-': # If your state board has a -, then replace the - with the cell value
			char=i+1 # i+1 since cell is based on 1 while char is based on 0
		new_board.append(char)
		
	# print cells as a string type with the border
	print('-------------')
	print('| {} | {} | {} |'.format(new_board[0], new_board[1], new_board[2]))
	print('-------------')
	print('| {} | {} | {} |'.format(new_board[3], new_board[4], new_board[5]))
	print('-------------')
	print('| {} | {} | {} |'.format(new_board[6], new_board[7], new_board[8])) 
	print('-------------')

# --------------------------------------------------
if __name__ == '__main__':
    main()
