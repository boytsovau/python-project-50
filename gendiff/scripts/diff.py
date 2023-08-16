import json
import yaml
import pathlib


def generate_diff(file1, file2, format='stylish'):

    data1 = open_file(file1, check_extension(file1))
    data2 = open_file(file2, check_extension(file2))

    def inner_diff(data1, data2, d=0):
        diff = {}
        for k, v in data1.items():
            if k in data2:
                if isinstance(data1[k], dict) and isinstance(data2[k], dict):
                    diff[f'  {k}'] = {'value': inner_diff(data1[k], data2[k], d + 1), 'deep': d + 1}
                elif data1[k] == data2[k]:
                    diff[f'  {k}'] = {'value': v, 'deep': d + 1}
                else:
                    diff[f'- {k}'] = {'value': v, 'deep': d + 1}
                    diff[f'+ {k}'] = {'value': data2[k], 'deep': d + 1}
            else:
                diff[f'- {k}'] = {'value': v, 'deep': d + 1}
        for k2, v2 in data2.items():
            if k2 not in data1:
                diff[f'+ {k2}'] = {'value': v2, 'deep': d + 1}
        return diff

    return inner_diff(data1, data2)


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
    print(generate_diff("./tests/fixtures/file3.json", "./tests/fixtures/file4.json"))
