import pytest
from gen_diff.scripts.diff import generate_diff

# Параметры для тестов
test_cases = [
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "expect.txt", "stylish"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yaml", "expect.txt", "stylish"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "res_stylish.txt", "stylish"),
    ("tests/fixtures/file3.yaml", "tests/fixtures/file4.yaml", "res_stylish.txt", "stylish"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "res_plain.txt", "plain"),
    ("tests/fixtures/file3.yaml", "tests/fixtures/file4.yaml", "res_plain.txt", "plain"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "res_json.txt", "json"),
]


@pytest.fixture
def expected(request):
    def load_expected(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return load_expected(f"tests/fixtures/{request.param}")


@pytest.mark.parametrize("file1, file2, expected, format", test_cases)
def test_generate_diff(file1, file2, expected, format):
    with open(f"tests/fixtures/{expected}", 'r') as file:
        expected_output = file.read()
    diff = generate_diff(file1, file2, format)
    assert diff == expected_output
