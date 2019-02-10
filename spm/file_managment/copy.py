from spm.config import Config


def __handle_file(scheme: str, id):
    print(scheme.format(id))

def copy_files(config: Config):
    for id in config.ids:
        __handle_file(config.file_scheme, id)
    pass