import json
import yaml
import pathlib


def get_data(file):
    extension = pathlib.PurePath(file).suffix.strip('.')
    content = open(file, "r")
    return parse(content, extension)


def parse(content, extension):
    if extension == 'json':
        return json.load(content)
    elif extension in ["yml", "yaml"]:
        return yaml.safe_load(content)
