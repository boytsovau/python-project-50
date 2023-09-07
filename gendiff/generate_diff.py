from gendiff.parser import get_data
from gendiff.generate_tree import gen_diff_tree
from gendiff.formaters.format_check import formater


def generate_diff(file1, file2, format='stylish'):

    data1 = get_data(file1)
    data2 = get_data(file2)

    diff = gen_diff_tree(data1, data2)
    return formater(diff, format)
