import json
import yaml
import pathlib


def get_extension(file):
    data = pathlib.PurePath(file).suffix.strip('.')
    return data


def read_file(file):
    with open(file) as f:
        return f.read()


def parse_json(content):
    return json.loads(content)


def parse_yaml(content):
    return yaml.safe_load(content)


def open_file(file, extension):
    content = read_file(file)
    if extension == 'json':
        return parse_json(content)
    elif extension in ["yml", "yaml"]:
        return parse_yaml(content)
