#!/usr/bin/env python3
import sys
import argparse
import os


def main(input_str=[], output_file=[]):
    '''
    Filter adjacent matching lines from INPUT (or standard input), writing to OUTPUT (or standard output).
    '''
    if len(input_str) == 1 and os.path.isfile(input_str[0]):
        with open(input_str[0], 'r') as f:
            file_lines = f.readlines()
            set_file = set(file_lines)

        if output_file:
            with open(output_file, 'w') as of:
                of.writelines(set_file)

        else:
            for line in set_file:
                sys.stdout.write(line)

    else:
        lines_set = set(input_str)

        if output_file:
            with open(output_file, 'w') as of:
                of.writelines(lines_set)

        for line in lines_set:
            sys.stdout.write(line + '\n')


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Filter adjacent matching lines from INPUT (or standard input), writing to OUTPUT (or standard output).'
    desc_two = 'The order in which lines are output is not guaranteed.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two]))
    parser.add_argument("input_str", nargs='*', default=sys.stdin, help="standard input or one file.")
    parser.add_argument("output_file", nargs='?', help="output file.")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        input_str = parser.parse_args().input_str.read().splitlines()
    else:
        input_str = args.input_str

    main(input_str=input_str,
         output_file=args.output_file)
