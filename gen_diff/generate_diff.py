from gen_diff.core import open_file, check_extension
from gen_diff.create_diff import get_diff
from gen_diff.format_check import formater


def generate_diff(file1, file2, format='stylish'):

    data1 = open_file(file1, check_extension(file1))
    data2 = open_file(file2, check_extension(file2))

    diff = get_diff(data1, data2)
    return formater(diff, format)
