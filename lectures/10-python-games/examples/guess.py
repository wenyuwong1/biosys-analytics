#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@gmail.com>
Purpose: Guess-the-number game
"""

import argparse
import random
import sys


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Guessing game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum value',
        metavar='int',
        type=int,
        default=1)

    parser.add_argument(
        '-x',
        '--max',
        help='Maximum value',
        metavar='int',
        type=int,
        default=50)

    parser.add_argument(
        '-g',
        '--guesses',
        help='Number of guesses',
        metavar='int',
        type=int,
        default=5)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    low = args.min
    high = args.max
    guesses_allowed = args.guesses
    secret = random.randint(low, high)

    if low < 1:
        print('--min cannot be lower than 1')
        sys.exit(1)

    if guesses_allowed < 1:
        print('--guesses cannot be lower than 1')
        sys.exit(1)

    if low > high:
        print('--min "{}" is higher than --max "{}"'.format(low, high))
        sys.exit(1)

    prompt = 'Guess a number between {} and {} (q to quit): '.format(low, high)
    num_guesses = 0

    while True:
        guess = input(prompt)
        num_guesses += 1

        if guess == 'q':
            print('Now you will never know the answer.')
            sys.exit(0)

        if not guess.isdigit():
            print('"{}" is not a number'.format(guess))
            continue

        print('You guessed "{}"'.format(guess))
        num = int(guess)

        if num_guesses >= guesses_allowed:
            print('Too many guesses! The number was "{}."'.format(secret))
            sys.exit()
        elif not low < num < high:
            print('Number is not in the allowed range')
        elif num == secret:
            print('You win!')
            break
        elif num < secret:
            print('Too low.')
        else:
            print('Too high.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
