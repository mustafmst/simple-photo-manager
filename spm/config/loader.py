import json

from spm.config import Config

def load_config(config_file_name) -> Config:
    with open(config_file_name) as j:
        data = json.load(j)
        return Config(data["file-scheme"], data["action"], data["from"], data["to"], data["ids"])