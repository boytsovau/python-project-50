import json
import yaml
import pathlib


def generate_diff(file1, file2):

    data1 = open_file(file1, check_extension(file1))
    data2 = open_file(file2, check_extension(file2))

    def inner_diff(data1, data2):
        diff = {}
        for k, v in data1.items():
            if k in data2:
                if isinstance(data1[k], dict) and isinstance(data2[k], dict):
                    diff[f'{k}'] = {'meta': {
                        'action': 'nested',
                        'children': inner_diff(data1[k], data2[k])}}
                elif data1[k] == data2[k]:
                    diff[f'{k}'] = {'meta': {
                        'value': v,
                        'action': 'unchanged'}}
                elif data1[k] != data2[k]:
                    diff[f'{k}'] = {'meta': {
                        'action': 'update',
                        "old_value": v,
                        "new_value": data2[k]}}
            else:
                if isinstance(v, dict):
                    diff[f'{k}'] = {'meta': {
                        'action': 'nested',
                        'children': inner_diff(v, {})}}
                else:
                    diff[f'{k}'] = {'meta': {
                        'value': v,
                        'action': 'delete'}}
        for k2, v2 in data2.items():
            if k2 not in data1:
                if isinstance(v2, dict):
                    diff[f'{k2}'] = {'meta': {
                        'action': 'nested',
                        'children': inner_diff({}, v2)}}
                else:
                    diff[f'{k2}'] = {'meta': {'values': v2, 'action': 'added'}}
        return diff
    return inner_diff(data1, data2)


def formater(diff, format='stylish'):
    if format == 'stylish':
        result = []

        def inner_format(data, depth=0):
            for key, val in data.items():
                action = val['meta']['action']
                if action == 'nested':
                    result.append(f"{'  ' * depth}  {key}: {{")
                    inner_format(val['meta']['children'], depth + 1)
                    result.append(f"{'  ' * depth}  }}")
                elif action == 'unchanged':
                    result.append(f"{'  ' * depth}  {key}: {val['meta']['value']}")
                elif action == 'update':
                    result.append(f"{'  ' * depth}- {key}: {val['meta']['old_value']}")
                    result.append(f"{'  ' * depth}+ {key}: {val['meta']['new_value']}")
                elif action == 'delete':
                    result.append(f"{'  ' * depth}- {key}: {val['meta']['value']}")
                elif action == 'added':
                    result.append(f"{'  ' * depth}+ {key}: {val['meta']['values']}")

        inner_format(diff)
        return '{\n' + '\n'.join(result) + '\n}'


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
    diff = generate_diff("./tests/fixtures/file3.json", "./tests/fixtures/file4.json")
    print(diff)
    print(formater(diff))
