import os.path as path

from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Express yourself with more than 140 characters")
    parser.add_argument("-f", "--file", type=str, help="Path of the file to be parsed", default=None)
    parser.add_argument("-m", "--message", type=str, help="Message to be parsed.", default=None)
    return parser


def get_text_from_file(path: str) -> str:
    if path.isfile(path):
        with open(path, 'r') as f:
            return f.read()


def get_text() -> str:
    parser = create_parser()
    args = parser.set_defaults(m=None, message=None, f=None, file=None)
    args = parser.parse_args()

    path = args.file or args.f
    message = args.m or args.message

    text = get_text_from_file(path) if path else message

    if not text:
        parser.print_help()

    return text
