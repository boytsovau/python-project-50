import argparse
import json


def generate_diff(file1, file2):
    data = []
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    data.append('{')
    for k, v in data1.items():
        if k in data2.keys() and v == data2.get(k):
            data.append(f'  {k}: {v}')
        if k in data2.keys() and v != data2.get(k):
            data.append(f'- {k}: {v}')
            data.append(f'+ {k}: {data2.get(k)}')
        if k not in data2.keys():
            data.append(f'- {k}: {v}')
    for k2, v2 in data2.items():
        if k2 not in data1.keys():
            data.append(f'+ {k2}: {v2}')
    data.append('}')
    return '\n'.join(data)


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
