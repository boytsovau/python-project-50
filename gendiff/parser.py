import argparse


def parser_args():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                            files and shows a difference')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        default='stylish', help='set format of output, \
                                            plain or json, stylish is default')

    return parser.parse_args()
