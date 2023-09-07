from gendiff.parser import get_data
from gendiff.compare_files import compare_data
from gendiff.formaters.format_check import formater


def generate_diff(file1, file2, format='stylish'):

    data1 = get_data(file1)
    data2 = get_data(file2)

    diff = compare_data(data1, data2)
    return formater(diff, format)
