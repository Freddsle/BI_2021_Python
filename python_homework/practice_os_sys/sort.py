#!/usr/bin/env python
import sys
import argparse
import re


def sort_human(stdin):
    '''
    Sort strings "human like", if they contain numbers.
    '''
    convert = lambda text: float(text) if text.isdigit() else text
    alphanum = lambda key: [convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]*)', key)]
    stdin.sort(key=alphanum)
    return stdin


def main(reverse_order=False, numeric=False, stdin=[]):
    '''
    Sorting stdin according to keys (reverse, numeric sort).
    '''
    if numeric:
        stdin = sort_human(stdin)

    else:
        stdin.sort()

    if reverse_order:
        stdin.reverse()

    for line in stdin:
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

    parser.add_argument('stdin', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    args = parser.parse_args()

    if not sys.stdin.isatty():
        stdin = parser.parse_args().stdin.read().splitlines()
    else:
        stdin = []

    main(reverse_order=args.reverse,
         numeric=args.numeric,
         stdin=stdin)
