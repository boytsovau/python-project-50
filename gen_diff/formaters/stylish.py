from gen_diff.core import get_offset, to_string

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
