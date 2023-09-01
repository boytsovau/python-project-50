import pytest
from gen_diff.scripts.diff import generate_diff


@pytest.mark.parametrize("file1, file2, expected", [
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "tests/fixtures/expected.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yaml", "tests/fixtures/expected.txt"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "tests/fixtures/expected3.txt"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "tests/fixtures/expected4.txt"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "tests/fixtures/expected5.txt")
])
def test_generate_diff(file1, file2, expected):
    with open(expected, 'r') as file:
        expected_result = file.read()
    diff = generate_diff(file1, file2)
    assert diff == expected_result
