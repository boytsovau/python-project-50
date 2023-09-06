import pytest
import os
from gendiff.generate_diff import generate_diff

FILE_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/fixtures"

# Параметры для тестов
test_cases = [
    (f"{FILE_PATH}/file1.json", f"{FILE_PATH}/file2.json", "expect.txt", None),
    (f"{FILE_PATH}/file1.yml", f"{FILE_PATH}/file2.yaml", "expect.txt", None),
    (f"{FILE_PATH}/file3.json", f"{FILE_PATH}/file4.json", "res_stylish.txt", "stylish"),
    (f"{FILE_PATH}/file3.yaml", f"{FILE_PATH}/file4.yaml", "res_stylish.txt", "stylish"),
    (f"{FILE_PATH}/file3.json", f"{FILE_PATH}/file4.json", "res_plain.txt", "plain"),
    (f"{FILE_PATH}/file3.yaml", f"{FILE_PATH}/file4.yaml", "res_plain.txt", "plain"),
    (f"{FILE_PATH}/file3.json", f"{FILE_PATH}/file4.json", "res_json.txt", "json"),
]


@pytest.mark.parametrize("file1, file2, expected, format", test_cases)
def test_generate_diff(file1, file2, expected, format):
    with open(f"{FILE_PATH}/{expected}", 'r') as file:
        expected_output = file.read()
        diff = generate_diff(file1, file2, format)
        assert expected_output == diff
