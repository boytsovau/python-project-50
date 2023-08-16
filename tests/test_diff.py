from gendiff.scripts.diff import generate_diff


def test_json():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") == expected


def test_yml():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
    assert generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yaml") == expected


def test_json():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
    assert generate_diff("tests/fixtures/file.json", "tests/fixtures/file2.json") == expected


def test_json_req():
    with open("tests/fixtures/expected3.txt", 'r') as file:
        expected = file.read()
    assert generate_diff("tests/fixtures/file3.json", "tests/fixtures/file4.json") == expected
