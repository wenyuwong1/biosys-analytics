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
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='---------')
    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str,
        choices=['X', 'x', 'O', 'o'],
        default='')
    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='int',
        type=int,
        choices=range(1, 10))
    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    state_arg = args.state
    player_arg = args.player
    cell_arg = args.cell

    board()

    if not state_is_ok(state_arg):
        print('"{}" must be 9 characters of only -, X, O'.format(state_arg))
        sys.exit(1)


# -------------------------------------------------
def state_is_ok(state):
    if len(state) != 9:
        return False

    elif ...:

    else:
        return True


# -------------------------------------------------
def board():

    # assign values to the different cells
    square = ['| 1 | 2 | 3 |\n', '| 4 | 5 | 6 |\n', '| 7 | 8 | 9 |\n']

    # print cells as a string type with the border

    print('-------------\n'.join([''] + square + ['']))


# --------------------------------------------------
if __name__ == '__main__':
    main()
