#!/usr/bin/env python3
import argparse
import os
import sys
import logging
from page_loader.loader import download
from page_loader.get_and_save_content import PageLoadError, \
    WebError, SysError

SUCCESSFUL_EXIT_CODE = 0
COMMON_ERROR_EXIT_CODE = 1
WEB_ERROR_EXIT_CODE = 2
WRITE_ERROR_EXIT_CODE = 3


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
    except PageLoadError as known_error:
        logging.error(str(known_error))
        if isinstance(known_error, WebError):
            sys.exit(WEB_ERROR_EXIT_CODE)
        elif isinstance(known_error, SysError):
            sys.exit(WRITE_ERROR_EXIT_CODE)
        else:
            sys.exit(COMMON_ERROR_EXIT_CODE)
    sys.exit(SUCCESSFUL_EXIT_CODE)


if __name__ == '__main__':
    main()
