### Hexlet tests and linter status:
[![Actions Status](https://github.com/boytsovau/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/boytsovau/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/0b02ed0c2f70e55fb3d0/maintainability)](https://codeclimate.com/github/boytsovau/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0b02ed0c2f70e55fb3d0/test_coverage)](https://codeclimate.com/github/boytsovau/python-project-50/test_coverage)
[![Actions Status](https://github.com/boytsovau/python-project-50/workflows/diff-test/badge.svg)](https://github.com/boytsovau/python-project-50/actions)

# Difference Calculator


The difference calculator is a program that determines the difference between two data structures.

Utility Features:

Support for different input formats: yaml, json
Generating a report in the form of plain text, stylish and json

# Install

    pip install --user git+https://github.com/boytsovau/python-project-50.git

# Usage:

    usage: gendiff [-h] [-f FORMAT] first_file second_file

    Compares two configuration files and shows a difference

    positional arguments:
      first_file
      second_file

    options:
      -h, --help            show this help message and exit
      -f FORMAT, --format FORMAT
                            set format of output, plain or json, stylish is default



# Example

[![asciicast](https://asciinema.org/a/606237.svg)](https://asciinema.org/a/606237)

#### stylish format

[![asciicast](https://asciinema.org/a/605434.svg)](https://asciinema.org/a/605434)

#### plain format

[![asciicast](https://asciinema.org/a/605790.svg)](https://asciinema.org/a/605790)


#### json format

[![asciicast](https://asciinema.org/a/605793.svg)](https://asciinema.org/a/605793)
