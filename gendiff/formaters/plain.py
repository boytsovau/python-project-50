def plain(data):
    return plain_format(data)


def plain_format(data, path=''):
    result = []
    for key, val in data.items():
        action = val.get('action')
        match action:
            case 'nested':
                result.append(plain_format(val['children'], f'{path}{key}.'))
            case 'added':
                result.append(f"Property '{path}{key}' "
                              f"was added with value: "
                              f"{to_string(val['value'])}")
            case 'delete':
                result.append(f"Property '{path}{key}' was removed")
            case 'update':
                result.append(f"Property '{path}{key}' was updated. "
                              f"From {to_string(val['old_value'])} "
                              f"to {to_string(val['new_value'])}")
    return '\n'.join(result)


def to_string(data):
    if isinstance(data, dict):
        return '[complex value]'
    if isinstance(data, bool):
        return str(data).lower()
    if data is None:
        return "null"
    if isinstance(data, str):
        return f"'{data}'"
    return str(data)
