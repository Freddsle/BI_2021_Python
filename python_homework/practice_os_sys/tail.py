#!/usr/bin/env python3
import sys
import argparse


def main(files, n_lines=10, filenames=True):
    '''
    Print the last "n_lines" lines of each FILE to standard output.
    '''
    if filenames:
        number_files = len(files)

        for file in files:

            if number_files > 1:
                sys.stdout.write(' '.join(['====>', file, '<====\n']))

            with open(file) as f:
                file_strings = f.readlines()
                file_len = len(file_strings)
                read_start = file_len - n_lines

                if read_start < 0:
                    read_start = 0

                for line in file_strings[read_start:]:
                    sys.stdout.write(line)

    else:
        file_len = len(files)
        read_start = file_len - n_lines
        if read_start < 0:
            read_start = 0

        for line in files[read_start:]:
            sys.stdout.write(line + '\n')


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Print the last 10 lines of each FILE to standard output.'
    desc_two = 'With more than one FILE, precede each with a header giving the file name.'
    desc_three = 'With no FILE read standard input.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two, desc_three]))

    parser.add_argument("-n", "--lines", default=10, type=int,
                        help="output the last NUM lines, instead of the last 10")
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
