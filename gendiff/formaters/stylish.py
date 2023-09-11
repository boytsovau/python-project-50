LEVEL_INDENT = 4
OFFSET = 2


def get_offset(depth):
    result = LEVEL_INDENT * depth - OFFSET
    return ' ' * result


def stylish(data):
    return stylish_format(data)


def stylish_format(data, depth=1):
    result = []
    for key, val in data.items():
        action = val.get('action')
        match action:
            case 'nested':
                result.append(f"{get_offset(depth)}  {key}: {{")
                result.append(stylish_format(val['children'], depth + 1))
                result.append(f"{get_offset(depth)}  }}")
            case 'unchanged':
                result.append(f"{get_offset(depth)}  {key}: {to_string(val['value'], depth)}")
            case 'update':
                result.append(f"{get_offset(depth)}- {key}: {to_string(val['old_value'], depth)}")
                result.append(f"{get_offset(depth)}+ {key}: {to_string(val['new_value'], depth)}")
            case 'delete':
                result.append(f"{get_offset(depth)}- {key}: {to_string(val['value'], depth)}")
            case 'added':
                result.append(f"{get_offset(depth)}+ {key}: {to_string(val['value'], depth)}")
    if depth == 1:
        result.insert(0, '{')
        result.append('}')
    return '\n'.join(result)


def to_string(value, depth=1):
    result = []
    if isinstance(value, dict):
        result.append('{')
        for key, val in value.items():
            result.append(f"{get_offset(depth + 1)}  {key}: {to_string(val, depth + 1)}")
        result.append(f"{get_offset(depth)}  }}")
        return '\n'.join(result)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, str):
        return value
