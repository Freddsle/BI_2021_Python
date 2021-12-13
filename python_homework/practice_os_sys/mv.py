#!/usr/bin/env python
import argparse
import shutil


def main(sourses, dir):
    '''
    Move or Rename SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.
    '''
    for sourse in sourses:
        shutil.move(sourse, dir)


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.'

    parser = argparse.ArgumentParser(description=desc_one)
    parser.add_argument("SOURCE", nargs='+', help="SOURCE path")
    parser.add_argument("DIRECTORY", help="DIRECTORY or DESTINATION path.")
    args = parser.parse_args()

    main(sourses=args.SOURCE,
         dir=args.DIRECTORY)
