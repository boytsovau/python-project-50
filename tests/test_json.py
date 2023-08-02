from gendiff.diff import generate_diff


def test_json():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") == expected
