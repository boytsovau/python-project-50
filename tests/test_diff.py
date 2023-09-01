import pytest
from gen_diff.scripts.diff import generate_diff


@pytest.fixture
def data_fixture():
    def load_data(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return load_data


@pytest.fixture
def expected_fixture():
    def load_expected(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return load_expected


def test_json(data_fixture, expected_fixture):
    data1 = data_fixture("tests/fixtures/file1.json")
    data2 = data_fixture("tests/fixtures/file2.json")
    expected = expected_fixture("tests/fixtures/expected.txt")
    diff = generate_diff(data1, data2)
    assert diff == expected


def test_yml(data_fixture, expected_fixture):
    data1 = data_fixture("tests/fixtures/file1.yml")
    data2 = data_fixture("tests/fixtures/file2.yaml")
    expected = expected_fixture("tests/fixtures/expected.txt")
    diff = generate_diff(data1, data2)
    assert diff == expected


def test_json_stylish(data_fixture, expected_fixture):
    data1 = data_fixture("tests/fixtures/file3.json")
    data2 = data_fixture("tests/fixtures/file4.json")
    expected = expected_fixture("tests/fixtures/expected3.txt")
    diff = generate_diff(data1, data2)
    assert diff == expected


def test_json_plain(data_fixture, expected_fixture):
    data1 = data_fixture("tests/fixtures/file3.json")
    data2 = data_fixture("tests/fixtures/file4.json")
    expected = expected_fixture("tests/fixtures/expected4.txt")
    diff = generate_diff(data1, data2, 'plain')
    assert diff == expected


def test_json_js(data_fixture, expected_fixture):
    data1 = data_fixture("tests/fixtures/file3.json")
    data2 = data_fixture("tests/fixtures/file4.json")
    expected = expected_fixture("tests/fixtures/expected5.txt")
    diff = generate_diff(data1, data2, 'json')
    assert diff == expected
