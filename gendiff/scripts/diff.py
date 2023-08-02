import json
import yaml
import pathlib


def generate_diff(file1, file2):

    data1 = open_file(file1, check_extension(file1))
    data2 = open_file(file2, check_extension(file2))
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


if __name__ == "__main__":
    generate_diff("./tests/fixtures/file1.json", "./tests/fixtures/file2.yaml")
