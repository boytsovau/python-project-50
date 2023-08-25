import json
import yaml
import pathlib


LEVEL_INDENT = 4
OFFSET = 2


def generate_diff(file1, file2):

    data1 = open_file(file1, check_extension(file1))
    data2 = open_file(file2, check_extension(file2))

    def inner_diff(data1, data2):
        diff = {}
        for k, v in data1.items():
            if k in data2:
                if isinstance(data1[k], dict) and isinstance(data2[k], dict):
                    diff[f'{k}'] = {
                        'action': 'nested',
                        'children': inner_diff(data1[k], data2[k])}
                elif data1[k] == data2[k]:
                    diff[f'{k}'] = {
                        'value': v,
                        'action': 'unchanged'}
                elif data1[k] != data2[k]:
                    diff[f'{k}'] = {
                        'action': 'update',
                        "old_value": v,
                        "new_value": data2[k]}
            else:
                diff[f'{k}'] = {
                    'value': v,
                    'action': 'delete'}
        for k2, v2 in data2.items():
            if k2 not in data1:
                diff[f'{k2}'] = {'value': v2, 'action': 'added'}
        return diff
    return inner_diff(data1, data2)


def formater(diff, format='stylish'):
    if format == 'stylish':
        result = []

        def inner_format(data, depth=1):
            for key, val in data.items():
                action = val.get('action')
                match action:
                    case 'nested':
                        result.append(f"{get_offset(depth)}  {key}: {{")
                        inner_format(val['children'], depth + 1)
                        result.append(f"{get_offset(depth)}}}")
                    case 'unchanged':
                        result.append(f"{get_offset(depth)}  {key}: {to_string(val['value'], depth)}")
                    case 'update':
                        result.append(f"{get_offset(depth)}- {key}: {to_string(val['old_value'], depth)}")
                        result.append(f"{get_offset(depth)}+ {key}: {to_string(val['new_value'], depth)}")
                    case 'delete':
                        result.append(f"{get_offset(depth)}- {key}: {to_string(val['value'], depth)}")
                    case 'added':
                        result.append(f"{get_offset(depth)}+ {key}: {to_string(val['value'], depth)}")

        inner_format(diff)
    return '{\n' + '\n'.join(result) + '\n}'


def to_string(value, depth=1):
    if isinstance(value, dict):
        result = '{\n'
        for key, val in value.items():
            result += f"{get_offset(depth + 1)}  {key}: {to_string(val, depth + 1)}\n"
        result += f"{get_offset(depth)}  }}"
    else:
        result = str(value)
    return result


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


if __name__ == "__main__":
    diff = generate_diff("./tests/fixtures/file3.json", "./tests/fixtures/file4.yaml")
    print(diff)
    print(formater(diff))
