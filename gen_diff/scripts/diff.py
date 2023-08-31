from gen_diff.core import open_file, check_extension
from gen_diff.formaters.stylish import stylish_format


def generate_diff(file1, file2, format='stylish'):

    data1 = open_file(file1, check_extension(file1))
    data2 = open_file(file2, check_extension(file2))

    diff = get_diff(data1, data2)
    return formater(diff, format)


diff = {}


def get_diff(data1, data2):
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


def formater(diff, format):
    if format == 'stylish':
        result = stylish_format(diff)
    return result


if __name__ == '__main__':
    diff = generate_diff("./tests/fixtures/file3.json", "./tests/fixtures/file4.yaml")
    print(diff)
