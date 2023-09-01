def get_diff(data1, data2):
    diff = {}
    for k in sorted(set(data1.keys()) | set(data2.keys())):
        if k in data1 and k in data2:
            if isinstance(data1[k], dict) and isinstance(data2[k], dict):
                diff[f'{k}'] = {
                    'action': 'nested',
                    'children': get_diff(data1[k], data2[k])}
            elif data1[k] == data2[k]:
                diff[f'{k}'] = {
                    'value': data1[k],
                    'action': 'unchanged'}
            else:
                diff[f'{k}'] = {
                    'action': 'update',
                    "old_value": data1[k],
                    "new_value": data2[k]}
        elif k in data1:
            diff[f'{k}'] = {
                'value': data1[k],
                'action': 'delete'}
        elif k in data2:
            diff[f'{k}'] = {
                'value': data2[k],
                'action': 'added'}
    return diff
