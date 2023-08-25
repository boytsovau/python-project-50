from gendiff.scripts.diff import generate_diff, formater


def test_json():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
        diff = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json") 
        assert formater(diff) == expected


def test_yml():
    with open("tests/fixtures/expected.txt", 'r') as file:
        expected = file.read()
    diff = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yaml")
    assert formater(diff) == expected


# def test_json_req():
#     with open("tests/fixtures/expected3.txt", 'r') as file:
#         expected = file.read()
#     diff = generate_diff("tests/fixtures/file3.json", "tests/fixtures/file4.json")
#     assert formater(diff) == expected

def test_json_req2():
    with open("tests/fixtures/result_stylish", 'r') as file:
        expected = file.read()
    diff = generate_diff("tests/fixtures/file5.json", "tests/fixtures/file6.json")
    assert formater(diff) == expected
