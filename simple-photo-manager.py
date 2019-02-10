import argparse

from spm.app_args import add_arguments
from spm.config.loader import load_config
from spm.file_managment.copy import copy_files

actions = dict(
    copy = copy_files
)

def main():
    parser = argparse.ArgumentParser(description="Simply manage Your photos")
    add_arguments(parser)
    args = parser.parse_args()

    config = load_config(args.config)

    actions[config.action](config)
    pass


if __name__ == "__main__":
    main()
