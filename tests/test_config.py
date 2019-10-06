from rambo.config import load_config, load_config_template
from schema import Schema, And, Use
from pathlib import Path

expected_config_template = Schema({
    "commands": {
        "action": {
            "help": And(Use(str)),
            "choices": And(Use(list))
        },
        "object": {
            "help": And(Use(str)),
            "choices": And(Use(list))
        }
    }
})

expected_config_values = {
    "commands": {
        "action": {
            "help": "place your actions (verbs) under action. eg, create, make, delete",
            "choices": ["create"]
        },
        "object": {
            "help": "place here the objects (nouns) which will be acted upon. eg file, migration, table",
            "choices": ["file"]
        }
    }
}

expected_rambo_config_values = {
    "commands": {
        "action": {
            "help": "available options for the rambo action argument",
            "choices": ["init", "delete"]
        },
        "object": {
            "help": "available options for the object argument",
            "choices": ["project", "file"]
        }
    }
}


def test_load_config_template():
    config_template = load_config_template()
    validated_config = expected_config_template.validate(config_template)
    assert validated_config == config_template


def test_load_rambo_config():
    rambo_config_path = Path(__file__).absolute().parent.parent / "rambo" / "config" / "rambo.yml"
    rambo_config = load_config(rambo_config_path)
    validated_rambo = expected_config_template.validate(rambo_config)
    assert validated_rambo == expected_rambo_config_values
