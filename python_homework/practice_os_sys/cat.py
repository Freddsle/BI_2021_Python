#!/usr/bin/env python
import sys
import argparse
import os


def main(files_lines, search_in=True):
    '''
    Concatenate strings to standard output. Default - concatenate the files content.
    '''
    for file in files_lines:
        if os.path.isfile(file) and search_in:
            with open(file) as origin_file:
                for line in origin_file:
                    sys.stdout.write(line)

        else:
            sys.stdout.write(file + '\n')


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Concatenate FILE(s) to standard output.'
    desc_two = 'With no FILE read standard input.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two]))
    parser.add_argument("files", nargs='*', default=sys.stdin, help="PATH to the FILEs.")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        files = parser.parse_args().stdin.read().splitlines()
        search_in = False
    else:
        files = args.files
        search_in = True

    main(files_lines=files,
         search_in=search_in)
