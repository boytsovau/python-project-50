def plain_format(data, path=''):
    result = []
    for key, val in data.items():
        action = val.get('action')
        match action:
            case 'nested':
                plain_format(val['children'], f'{path}{key}.')
            case 'added':
                result.append(f"Property '{path}{key}' was added with value: "
                              f"{check_val(val['value'])}")
            case 'delete':
                result.append(f"Property '{path}{key}' was removed")
            case 'update':
                result.append(f"Property '{path}{key}' was updated. "
                              f"From {check_val(val['old_value'])} "
                              f"to {check_val(val['new_value'])}")
    return '\n'.join(result)


def check_val(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return "null"
    else:
        return f"'{str(data)}'"
