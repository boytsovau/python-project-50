from gen_diff.formaters.stylish import stylish_format
from gen_diff.formaters.plain import plain_format
from gen_diff.formaters.js import json_format


def formater(diff, format):
    if format == 'plain':
        return plain_format(diff)
    elif format == 'json':
        return json_format(diff)
    else:
        return stylish_format(diff)