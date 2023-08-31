import json
import yaml
import pathlib

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


def to_string(value, depth=1):
    if isinstance(value, dict):
        result = '{\n'
        for key, val in value.items():
            result += f"{get_offset(depth + 1)}  {key}: {to_string(val, depth + 1)}\n"
        result += f"{get_offset(depth)}  }}"
    elif isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = "null"
    else:
        result = str(value)
    return result
