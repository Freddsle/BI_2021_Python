#!/usr/bin/env python3
import sys
import argparse
import re


def count_bytes(stdin):
    '''
    Count bytes in stdin using system dafault encodind.
    '''
    bytes_number = len(stdin.encode(sys.getdefaultencoding()))
    return str(bytes_number)


def count_words(stdin):
    '''
    Count words in stdin.
    A word is a non-zero-length sequence of characters delimited by white space.
    Words at the end of the file without trailing new lines are also counted.
    '''
    pattern = re.compile(r'(?:(?<=^)|(?<=\s))[\S]+(?:(?=$)|(?=\s))')
    words_number = len(re.findall(pattern, stdin))
    return str(words_number)


def main(lines=False, words=False, bytes=False, stdin=[]):
    '''
    Calculate number of lines, words, byted and prints the result to standard output.
    '''
    if lines:
        sys.stdout.write(str(len(stdin.splitlines())) + '\n')

    if words:
        words_number = count_words(stdin)
        sys.stdout.write(words_number + '\n')

    if bytes:
        sys.stdout.write(count_bytes(stdin) + '\n')


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Print newline, word, and byte counts for each FILE.'
    desc_two = 'A word is a non-zero-length sequence of characters delimited by white space.'
    desc_three = 'Words at the end of the file without trailing "\n" are also counted.'
    desc_four = 'If multiple arguments are passed, the output is in "lines", "words", "bytes" order. Each in new line.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two, desc_three, desc_four]))

    parser.add_argument("-l", "--lines", help="print the newline counts", action="store_true")
    parser.add_argument("-w", "--words", help="print the word counts", action="store_true")
    parser.add_argument("-c", "--bytes", help="print the byte counts used system encoding", action="store_true")

    parser.add_argument('stdin', nargs='?', default=sys.stdin)

    args = parser.parse_args()

    if not sys.stdin.isatty():
        stdin = parser.parse_args().stdin.read()
    else:
        stdin = []

    main(lines=args.lines,
         words=args.words,
         bytes=args.bytes,
         stdin=stdin)
