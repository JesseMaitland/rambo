import argparse
from rambo.config import load_config
from pathlib import Path


def _get_arg_parser(commands: dict):
    parser = argparse.ArgumentParser()
    for command, options in commands["commands"].items():
        parser.add_argument(command, **options)
    return parser.parse_args()


def provide_func_key(path: Path = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            config = load_config(path)
            cmd_args = _get_arg_parser(config)
            func_key = f"{cmd_args.action}_{cmd_args.object}"
            return func(func_key=func_key, *args, **kwargs)
        return wrapper
    return decorator


def provide_config(path: Path = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            config = load_config(path)
            return func(config=config, *args, **kwargs)
        return wrapper
    return decorator


def provide_cmd_args(path: Path = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            config = load_config(path)
            cmd_args = _get_arg_parser(config)
            return func(cmd_args=cmd_args, *args, **kwargs)
        return wrapper
    return decorator
