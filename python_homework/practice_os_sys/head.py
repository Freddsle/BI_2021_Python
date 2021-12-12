#!/usr/bin/env python
import sys
import argparse


def main(files, n_lines=10, filenames=True):
    '''
    Print the first "n_lines" lines of each FILE to standard output.
    '''
    if filenames:
        number_files = len(files)

        for file in files:
            if number_files > 1:
                sys.stdout.write(' '.join(['====>', file, '<====\n']))

            with open(file) as f:
                counter = 0

                for line in f:
                    if counter < n_lines:
                        sys.stdout.write(line)
                        counter += 1
                    else:
                        break

    else:

        for i, line in enumerate(files):
            if i < n_lines:
                sys.stdout.write(line + '\n')
            else:
                break


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Print the first 10 lines of each FILE to standard output.'
    desc_two = 'With more than one FILE, precede each with a header giving the file name.'
    desc_three = 'With no FILE read standard input.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two, desc_three]))

    parser.add_argument("-n", "--lines", default=10, type=int,
                        help="output the last NUM lines, instead of the first 10")
    parser.add_argument("files", nargs='*', default=sys.stdin, help="PATH to the FILEs.")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        files = parser.parse_args().files.read().splitlines()
        filenames = False
    else:
        files = args.files
        filenames = True

    main(files=files,
         n_lines=args.lines,
         filenames=filenames)
