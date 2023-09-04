import json
import yaml
import pathlib
import argparse


LEVEL_INDENT = 4
OFFSET = 2


def get_offset(depth):
    result = LEVEL_INDENT * depth - OFFSET
    return ' ' * result


def check_extension(file):
    data = pathlib.PurePath(file).suffix.strip('.')
    return data


def open_file(file, extension):
    if extension == 'json':
        with open(file) as f:
            data = json.load(f)
        return data
    if extension == "yml" or "yaml":
        with open(file) as f:
            data = yaml.safe_load(f)
        return data


def parser_args():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                            files and shows a difference')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument( '-f', '--format', metavar='FORMAT',
                         default='stylish', help='set format of output, \
                                            plain or json, stylish is default')

    return parser.parse_args()
