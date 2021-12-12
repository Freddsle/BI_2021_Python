#!/usr/bin/env python
import os
import argparse
import sys
import re


def find_regexp(line, patterns, search_in):
    '''
    Check for pattern in line. If present - print line to stdout.
    '''
    print_if = False

    for pattern in patterns:
        if re.search(pattern, line):
            print_if = True
            break

    if print_if and search_in:
        sys.stdout.write(line)
        
    if print_if and not search_in:
        sys.stdout.write(line + '\n')


def main(patterns, files_lines, search_in):
    '''
    Find patterns in input. Print lines with it to stdout.
    '''
    patterns = [re.compile(x) for x in patterns.split("|")]

    for file in files_lines:
        if os.path.isfile(file) and search_in:
            with open(file) as origin_file:
                for line in origin_file:
                    find_regexp(line, patterns, search_in)

        else:
            find_regexp(file, patterns, search_in)


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Search for PATTERNS in each FILE.'
    desc_two = 'PATTERNS can contain multiple patterns separated with pipes, "|", but printed in one string.'
    desc_three = 'The line will be printed if at least one pattern is found.'
    desc_four = 'When no FILE read standard input.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two, desc_three, desc_four]))
    parser.add_argument("patterns", help="patterns in Python RegExp style.")
    parser.add_argument("files", nargs='*', default=sys.stdin, help="PATH to the FILEs.")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        files = parser.parse_args().files.read().splitlines()
        search_in = False
    else:
        files = args.files
        search_in = True

    main(patterns=args.patterns,
         files_lines=files,
         search_in=search_in)
