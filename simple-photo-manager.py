import argparse

from spm.app_args import add_arguments
from spm.config.loader import load_config


def main():
    parser = argparse.ArgumentParser(description="Simply manage Your photos")
    add_arguments(parser)
    args = parser.parse_args()

    config = load_config(args.config)

    print(config.file_scheme.format(config.ids[0]))
    pass


if __name__ == "__main__":
    main()
