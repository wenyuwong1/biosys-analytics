#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@gmail.com>
Purpose: Hangman game
"""

import argparse
import os
import random
import re
import sys


# --------------------------------------------------
def get_args():
    """parse arguments"""
    parser = argparse.ArgumentParser(
        description='Hangman',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-l', '--maxlen', help='Max word length', type=int, default=10)

    parser.add_argument(
        '-n', '--minlen', help='Min word length', type=int, default=5)

    parser.add_argument(
        '-m', '--misses', help='Max number of misses', type=int, default=10)

    parser.add_argument(
        '-w',
        '--wordlist',
        help='Word list',
        type=str,
        default='/usr/share/dict/words')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    max_len = args.maxlen
    min_len = args.minlen
    max_misses = args.misses
    wordlist = args.wordlist

    if not os.path.isfile(wordlist):
        print('--wordlist "{}" is not a file.'.format(wordlist))
        sys.exit(1)

    if min_len < 1:
        print('--minlen must be positive')
        sys.exit(1)

    if not 3 <= max_len <= 20:
        print('--maxlen should be between 3 and 20')
        sys.exit(1)

    if min_len > max_len:
        print('--minlen ({}) is greater than --maxlen ({})'.format(
            min_len, max_len))
        sys.exit(1)

    regex = re.compile('^[a-z]{' + str(min_len) + ',' + str(max_len) + '}$')
    words = [w for w in open(wordlist).read().split() if regex.match(w)]
    word = random.choice(words)
    play({'word': word, 'max_misses': max_misses})


# --------------------------------------------------
def play(state):
    """Loop to play the game"""
    word = state.get('word') or ''

    if not word:
        print('No word!')
        sys.exit(1)

    guessed = state.get('guessed') or list('_' * len(word))
    prev_guesses = state.get('prev_guesses') or set()
    num_misses = state.get('num_misses') or 0
    max_misses = state.get('max_misses') or 0

    if ''.join(guessed) == word:
        msg = 'You win. You guessed "{}" with "{}" miss{}!'
        print(msg.format(word, num_misses, '' if num_misses == 1 else 'es'))
        sys.exit(0)

    if num_misses >= max_misses:
        print('You lose, loser!  The word was "{}."'.format(word))
        sys.exit(0)

    print('{} (Misses: {})'.format(' '.join(guessed), num_misses))
    new_guess = input('Your guess? ("?" for hint, "!" to quit) ').lower()

    if new_guess == '!':
        print('Better luck next time, loser.')
        sys.exit(0)
    elif new_guess == '?':
        new_guess = random.choice([x for x in word if x not in guessed])
        num_misses += 1

    if not re.match('^[a-zA-Z]$', new_guess):
        print('"{}" is not a letter'.format(new_guess))
        num_misses += 1
    elif new_guess in prev_guesses:
        print('You already guessed that')
    elif new_guess in word:
        prev_guesses.add(new_guess)
        last_pos = 0
        while True:
            pos = word.find(new_guess, last_pos)
            if pos < 0:
                break
            elif pos >= 0:
                guessed[pos] = new_guess
                last_pos = pos + 1
    else:
        num_misses += 1

    play({
        'word': word,
        'guessed': guessed,
        'num_misses': num_misses,
        'prev_guesses': prev_guesses,
        'max_misses': max_misses
    })


# --------------------------------------------------
if __name__ == '__main__':
    main()
