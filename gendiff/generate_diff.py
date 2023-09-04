from gendiff.core import open_file, check_extension
from gendiff.create_diff import get_diff
from gendiff.format_check import formater


def generate_diff(file1, file2, format='stylish'):

    data1 = open_file(file1, check_extension(file1))
    data2 = open_file(file2, check_extension(file2))

    diff = get_diff(data1, data2)
    return formater(diff, format)
