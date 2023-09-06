from gendiff.core import open_file, get_extension
from gendiff.compare_files import compare_data
from gendiff.formaters.format_check import formater


def generate_diff(file1, file2, format='stylish'):

    data1 = open_file(file1, get_extension(file1))
    data2 = open_file(file2, get_extension(file2))

    diff = compare_data(data1, data2)
    return formater(diff, format)
