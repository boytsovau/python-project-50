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


if __name__ == '__main__':
    data = {'common': {'action': 'nested', 'children': {'follow': {'value': False, 'action': 'added'}, 'setting1': {'value': 'Value 1', 'action': 'unchanged'}, 'setting2': {'value': 200, 'action': 'delete'}, 'setting3': {'action': 'update', 'old_value': True, 'new_value': None}, 'setting4': {'value': 'blah blah', 'action': 'added'}, 'setting5': {'value': {'key5': 'value5'}, 'action': 'added'}, 'setting6': {'action': 'nested', 'children': {'doge': {'action': 'nested', 'children': {'wow': {'action': 'update', 'old_value': '', 'new_value': 'so much'}}}, 'key': {'value': 'value', 'action': 'unchanged'}, 'ops': {'value': 'vops', 'action': 'added'}}}}}, 'group1': {'action': 'nested', 'children': {'baz': {'action': 'update', 'old_value': 'bas', 'new_value': 'bars'}, 'foo': {'value': 'bar', 'action': 'unchanged'}, 'nest': {'action': 'update', 'old_value': {'key': 'value'}, 'new_value': 'str'}}}, 'group2': {'value': {'abc': 12345, 'deep': {'id': 45}}, 'action': 'delete'}, 'group3': {'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}, 'action': 'added'}}
    print(stylish_format(data))