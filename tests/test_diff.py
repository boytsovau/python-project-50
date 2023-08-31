from gen_diff.scripts.diff import generate_diff


def test_json():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
        diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") 
        assert diff == expected


def test_yml():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
        diff = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yaml")
        assert diff == expected


def test_json_stylish():
    with open("tests/fixtures/expected3.txt", 'r') as file:
        expected = file.read()
        diff = generate_diff("tests/fixtures/file3.json", "tests/fixtures/file4.json")
        assert diff == expected


def test_json_plain():
    with open("tests/fixtures/expected4.txt", 'r') as file:
        expected = file.read()
        diff = generate_diff("tests/fixtures/file3.json", "tests/fixtures/file4.json", 'plain')
        assert diff == expected



