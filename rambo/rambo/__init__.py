from pathlib import Path
import yaml
from rambo.config import load_config_template


def init_project():
    action_path = Path.cwd().absolute() / "actions"
    action_path.mkdir(parents=True, exist_ok=True)

    config_template = load_config_template()
    config_path = Path.cwd().absolute() / "rambo.yml"
    config_path.touch()
    yaml.dump(data=config_template, stream=config_path.open(mode="w"))
