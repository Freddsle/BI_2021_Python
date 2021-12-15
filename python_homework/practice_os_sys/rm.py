#!/usr/bin/env python3
import os
import argparse
import shutil
import sys


def main(recursive=False, dir=False, paths=[]):
    '''
    Remove the FILE(s) or DIR(s).
    '''
    for path in paths:

        if os.path.isfile(path) and not dir:
            os.remove(path)

        elif dir:
            if recursive:
                shutil.rmtree(path)
            else:
                try:
                    os.rmdir(path)
                except OSError:
                    sys.stdout.write('cannot remove ' + path + ': Directory not empty' + '\n')

        elif not dir and os.path.isdir(path):
            sys.stdout.write('cannot remove ' + path + ': Is a directory' + '\n')


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Remove the FILE(s) or DIRs. Remove directories with option "-d".'
    desc_two = 'If directory is not empty - "-r" ortion should used to remove dir recursively.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two]))

    parser.add_argument("-r", "--recursive",
                        help="remove directories and their contents recursively",
                        action="store_true")

    parser.add_argument("-d", "--dir", help="remove empty directories", action="store_true")
    parser.add_argument("path", nargs='+', default=sys.stdin, help="PATH to the FILEs or directory.")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        path = parser.parse_args().stdin.read().splitlines()
    else:
        path = args.path

    main(recursive=args.recursive,
         dir=args.dir,
         paths=path)
