from os import getcwd, makedirs
from shutil import copyfile

from spm.config import Config


def __handle_file(config: Config, id):
    print(
        'Coping file {} to {}'.format(
            config.file_scheme.format(id), 
            '{}/{}'.format(getcwd(),config.to_path)))
    copyfile(
        src='{}/{}/{}'.format(getcwd(),config.from_path, config.file_scheme.format(id)),
        dst='{}/{}/{}'.format(getcwd(), config.to_path, config.file_scheme.format(id)))

def copy_files(config: Config):
    makedirs('{}/{}'.format(getcwd(), config.to_path), exist_ok=True)
    for id in config.ids:
        __handle_file(config, id)
    pass