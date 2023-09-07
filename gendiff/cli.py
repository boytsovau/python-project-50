import argparse
import textwrap


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
    Compares two configuration files and shows a difference

    Support file extension: json, yml, yaml
    '''))
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        default='stylish', help='set format of output, \
                                            plain or json, stylish is default')

    return parser.parse_args()
