#!/usr/bin/env python3
import argparse
import os
import sys
import logging
from page_loader.loader import download


def main():
    parser = argparse.ArgumentParser(description='Loading page content')
    parser.add_argument('url')
    parser.add_argument('-o', '--output',
                        action='store',
                        dest='path',
                        metavar='OUTPUT',
                        default=os.getcwd(),
                        help='set output dir and url',
                        type=str)
    args = parser.parse_args()
    try:
        result = download(args.url, args.path)
        print(result)
    except Exception:
        logging.exception('Exception occurred')
        sys.exit(1)


if __name__ == '__main__':
    main()
