#!/usr/bin/env python
import os
import argparse


def main(target, link_name, symbolic=False):
    '''
    Create a link to TARGET with the name LINK_NAME.
    '''
    if symbolic:
        os.symlink(target, link_name)

    else:
        os.link(target, link_name)


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    desc_one = 'Create a link to TARGET with the name LINK_NAME.'
    desc_two = 'Create hard links by default, symbolic links with --symbolic.'
    desc_three = 'Each destination (name of new link) should not already exist.'
    desc_four = 'When creating hard links, each TARGET must exist.'

    parser = argparse.ArgumentParser(description=' '.join([desc_one, desc_two, desc_three, desc_four]))

    parser.add_argument("-s", "--symbolic", help="make symbolic links instead of hard links", action="store_true")
    parser.add_argument("TARGET", help="TARGET path")
    parser.add_argument("LINK_NAME", help="link name.")
    args = parser.parse_args()

    main(symbolic=args.symbolic,
         target=args.TARGET,
         link_name=args.LINK_NAME)
