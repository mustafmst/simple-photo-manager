from os import getcwd, makedirs, path
from shutil import copyfile

from spm.config import Config


def get_path_from(config: Config):
    return path.join(getcwd(), config.from_path)


def get_path_to(config: Config):
    return path.join(getcwd(), config.to_path)


def get_file_name(config: Config, id: str):
    return config.file_scheme.format(id)


def __handle_file(config: Config, id):
    file_name = get_file_name(config, id)
    path_to = get_path_to(config)
    path_from = get_path_from(config)

    print(
        'Coping file {} to {}'.format(
            file_name, 
            path_to))

    copyfile(
        src=path.join(path_from, file_name),
        dst=path.join(path_to, file_name))


def copy_files(config: Config):
    makedirs(get_path_to(config), exist_ok=True)
    for id in config.ids:
        __handle_file(config, id)
