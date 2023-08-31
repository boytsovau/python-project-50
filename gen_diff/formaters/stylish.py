from gen_diff.core import get_offset


result = []


def stylish_format(data, depth=1):
    for key, val in data.items():
        action = val.get('action')
        match action:
            case 'nested':
                result.append(f"{get_offset(depth)}  {key}: {{")
                stylish_format(val['children'], depth + 1)
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
    return '{\n' + '\n'.join(result) + '\n}'


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
