from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.js import json_format


def formater(diff, format):
    if format == 'plain':
        return plain(diff)
    elif format == 'json':
        return json_format(diff)
    else:
        return stylish(diff)
