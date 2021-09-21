import argparse
import os
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
    result = download(args.url, args.path)
    print(result)


if __name__ == '__main__':
    main()
