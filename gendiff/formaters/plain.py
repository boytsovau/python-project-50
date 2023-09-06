def plain(data):
    result = []
    plain_format(data, result)
    return '\n'.join(result)


def plain_format(data, result, path=''):
    for key, val in data.items():
        action = val.get('action')
        match action:
            case 'nested':
                plain_format(val['children'], result, f'{path}{key}.')
            case 'added':
                result.append(f"Property '{path}{key}' "
                              f"was added with value: "
                              f"{get_val(val['value'])}")
            case 'delete':
                result.append(f"Property '{path}{key}' was removed")
            case 'update':
                result.append(f"Property '{path}{key}' was updated. "
                              f"From {get_val(val['old_value'])} "
                              f"to {get_val(val['new_value'])}")


def get_val(data):
    if isinstance(data, dict):
        return '[complex value]'
    if isinstance(data, bool):
        return str(data).lower()
    if data is None:
        return "null"
    if isinstance(data, str):
        return f"'{data}'"
    else:
        return str(data)
