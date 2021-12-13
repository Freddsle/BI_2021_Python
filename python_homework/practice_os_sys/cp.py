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
            files_for_copy = os.listdir(sourse)
            for file in files_for_copy:
                shutil.copytree(file, dir)

        else:
            try:
                shutil.copy(sourse, dir)

            except OSError:
                if not os.path.isfile(sourse):
                    sys.stdout.write('SOURCE is a DIRECTORY. Use --recursive option.\n')

                elif not os.path.exists(dir):
                    os.makedirs(dir, exist_ok=True)
                    shutil.copy(sourse, dir)


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
