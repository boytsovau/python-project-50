import json
import yaml
import pathlib


def get_data(file):
    extension = pathlib.PurePath(file).suffix.strip('.')
    with open(file) as f:
        content = f.read()
    return parse(content, extension)


def parse(content, extension):
    if extension == 'json':
        return json.loads(content)
    elif extension in ["yml", "yaml"]:
        return yaml.safe_load(content)
    else:
        raise ValueError(f"File has incorrect extension '{extension}'."
                         f" Use gendiff -h for help")
