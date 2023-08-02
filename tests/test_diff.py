from gendiff.scripts.diff import generate_diff


def test_json():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") == expected


def test_yml():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
    assert generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yaml") == expected


def test_same():
    with open("tests/fixtures/expected2.txt", 'r') as file:
        expected = file.read()
    # assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file1.yml") == expected
    assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file1.json") == expected


# def test_all():
#     with open("tests/fixtures/expected.txt", 'r') as file:
#         expected = file.read()
#     assert generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.yaml") == expected
