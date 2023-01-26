#!/usr/bin/env python

import argparse
from react_extractor.main import extractor


def main():
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--apk', help='APK file', required=True)

    args = parser.parse_args()

    extractor(args.apk)

if __name__ == '__main__':
    main()