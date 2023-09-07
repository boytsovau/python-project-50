from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json_format


def formater(diff, format):
    if format == 'plain':
        return plain(diff)
    elif format == 'json':
        return json_format(diff)
    elif format == 'stylish':
        return stylish(diff)
    else:
        raise ValueError(f"Command contains invalid format '{format}'."
                         f" Use gendiff -h for help")
