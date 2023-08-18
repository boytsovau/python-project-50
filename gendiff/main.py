import argparse
from gendiff.scripts.diff import generate_diff, formater


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                            files and shows a difference')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--f', '--format', metavar='FORMAT', default='stylish', help='set format of output')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    result = formater(diff, args.f)
    print(result)

