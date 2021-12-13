#!/usr/bin/env python
import os
import argparse
import shutil
import sys


def main(sourses, dir, recursive=False):
    '''
    Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.
    '''
    for sourse in sourses:
        if recursive:
            shutil.copytree(sourse, dir)

        else:
            try:
                shutil.copy2(sourse, dir)

            except OSError:
                if not os.path.isfile(sourse):
                    sys.stdout.write('SOURCE is a DIRECTORY. Use --recursive option.\n')


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.'

    parser = argparse.ArgumentParser(description=desc_one)

    parser.add_argument("-r", "--recursive", help="copy directories recursively to DIRECTORY", action="store_true")
    parser.add_argument("SOURCE", nargs='+', help="SOURCE path")
    parser.add_argument("DIRECTORY", help="DIRECTORY or DESTINATION path.")
    args = parser.parse_args()

    main(recursive=args.recursive,
         sourses=args.SOURCE,
         dir=args.DIRECTORY)
