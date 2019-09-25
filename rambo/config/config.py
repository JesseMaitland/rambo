import yaml
from pathlib import Path


def load_config(path=None):
    if not path:
        config_filename = "rambo.yml"
        path = Path().cwd().absolute() / config_filename
    return yaml.safe_load(path.open())


def load_config_template():
    config_filename = "config_template.yml"
    path = Path(__file__).absolute().parent / config_filename
    return yaml.safe_load(path.open())
