import pytest
import os
from gendiff.generate_diff import generate_diff

FIXTURE_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/fixtures"

# Параметры для тестов
test_cases = [
    ("file1.json", "file2.json", "expect.txt", "stylish"),
    ("file1.yml", "file2.yaml", "expect.txt", "stylish"),
    ("file3.json", "file4.json", "res_stylish.txt", "stylish"),
    ("file3.yaml", "file4.yaml", "res_stylish.txt", "stylish"),
    ("file3.json", "file4.json", "res_plain.txt", "plain"),
    ("file3.yaml", "file4.yaml", "res_plain.txt", "plain"),
    ("file3.json", "file4.json", "res_json.txt", "json"),
]


def gen_full_path(file):
    return f"{FIXTURE_PATH}/{file}"


@pytest.mark.parametrize("file1, file2, expected, format", test_cases)
def test_generate_diff(file1, file2, expected, format):
    with open(gen_full_path(expected), 'r') as file:
        expected_output = file.read()
        diff = generate_diff(gen_full_path(file1), gen_full_path(file2), format)
        assert expected_output == diff
