#!/usr/bin/env python
import sys
import os
import argparse
import re


def main(all=False, directory=os.getcwd()):
    '''
    Print the files and folders in directory.
    '''
    if type(directory) == list and len(directory) == 1:
        directory = directory[0]

    paths = sorted(os.listdir(path=directory))

    if os.path.exists('./') and all:
        sys.stdout.write('.' + '\t')

    if os.path.exists('../') and all:
        sys.stdout.write('..' + '\t')

    for path in paths:        
        if re.match(r'^\..*', path):
            if all:
                sys.stdout.write(path + '\t')
        else:
            sys.stdout.write(path + '\t')

    sys.stdout.write('\n')


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'List information about the FILEs (from the current directory by default).'
    desc_two = 'Sort entries.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two]))

    parser.add_argument("-a", "--all", help="do not ignore entries starting with .", action="store_true")
    parser.add_argument("directory", nargs='?', default=os.getcwd(), help="PATH. the current directory by default.")
    args = parser.parse_args()

    main(all=args.all,
         directory=args.directory)
