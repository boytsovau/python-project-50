import argparse
import json


def generate_diff(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    diff = {}

    for k, v in data1.items():
        if k in data2:
            if v == data2[k]:
                diff[f'  {k}'] = v
            else:
                diff[f'- {k}'] = v
                diff[f'+ {k}'] = data2[k]
        else:
            diff[f'- {k}'] = v

    for k2, v2 in data2.items():
        if k2 not in data1:
            diff[f'+ {k2}'] = v2

    return '{\n' + '\n'.join([f'{key}: {val}' for key, val in diff.items()]) + '\n}'


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                            files and shows a difference')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--f', '--format', metavar='FORMAT', help='set format of output')

    args = parser.parse_args()
    print(args)
    result = generate_diff(args.first_file, args.second_file)
    print(result)
