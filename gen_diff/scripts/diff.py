from gen_diff.generate_diff import generate_diff
from gen_diff.core import parser_args


def main():
    args = parser_args()
    print(generate_diff(args.first_file, args.second_file, args.f))
