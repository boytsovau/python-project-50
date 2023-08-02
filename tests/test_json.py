from gendiff.diff import generate_diff

def test_json():
    expected = '''{
  host: hexlet.io
- timeout: 50
+ timeout: 20
- proxy: 123.234.53.22
- follow: False
+ verbose: True
}'''
    assert generate_diff("tests/file1.json", "tests/file2.json") == expected
