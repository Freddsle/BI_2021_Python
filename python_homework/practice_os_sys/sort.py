#!/usr/bin/env python
import sys
import argparse
import re
import os


def convert(text):
    if text.isdigit():
        return float(text)  
    else:
        return text


def alphanum(key):
    return [convert(c) for c in re.split(r'([-+]?[0-9]*\.?[0-9]*)', key)]        


def sort_human(stdin):
    '''
    Sort strings "human like", if they contain numbers.
    '''
    stdin.sort(key=alphanum)
    return stdin


def main(reverse_order=False, numeric=False, stdin=[], file_end=False):
    '''
    Sorting stdin according to keys (reverse, numeric sort).
    '''
    if isinstance(stdin, str) and os.path.isfile(stdin):
        file_end = True

        with open(stdin, 'r') as f:
            stdin = f.readlines()

    if numeric:
        stdin = sort_human(stdin)

    else:
        stdin.sort()

    if reverse_order:
        stdin.reverse()

    for line in stdin:
        if file_end:
            sys.stdout.write(line)
        else:        
            sys.stdout.write(line + '\n')


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Write sorted concatenation of all FILE(s) to standard output.\n\n'
    desc_two = 'With no FILE, or when FILE is -, read standard input.'
    desc_three = 'The locale specified by the environment affects sort order.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two, desc_three]))

    parser.add_argument("-r", "--reverse", help="reverse the result of comparisons", action="store_true")
    parser.add_argument("-n", "--numeric", help="compare according to string numerical value", action="store_true")

    parser.add_argument('stdin', nargs='?', default=sys.stdin)

    args = parser.parse_args()

    if not sys.stdin.isatty():
        stdin = parser.parse_args().stdin.read().splitlines()
    else:
        stdin = args.stdin

    main(reverse_order=args.reverse,
         numeric=args.numeric,
         stdin=stdin)
