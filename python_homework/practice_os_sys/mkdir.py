#!/usr/bin/env python
import os
import argparse
import sys


def main(directories, parents=False):
    '''
    Create DIR(s).
    '''
    for directory in directories:

        if not parents:
            try:
                os.mkdir(directory)

            except FileExistsError:
                sys.stdout.write(' '.join(['cannot create directory:', directory, ': File exists\n']))

            except FileNotFoundError:
                sys.stdout.write(' '.join(['cannot create directory:', directory, ': No such file or directory\n']))
                sys.stdout.write('Use "-p option.\n')

        else:
            os.makedirs(directory, exist_ok=True)


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Create the DIRECTORY(ies), if they do not already exist.'
    desc_two = 'If you need to create directory in subdirectory - use "-p" option.'

    parser = argparse.ArgumentParser(description=desc_one)

    parser.add_argument("-p", "--parents", 
                        help="no error if existing, make parent directories as needed", 
                        action="store_true")

    parser.add_argument("directories", nargs='+', default=sys.stdin, help="directories names.")
    args = parser.parse_args()

    main(parents=args.parents,
         directories=args.directories)
