from rambo.mapper import function_mapper
from rambo.terminal import provide_func_key, provide_config
import rambo.rambo as rambo
from pathlib import Path

rambo_config_path = Path(__file__).absolute().parent.parent / "config" / "rambo.yml"


@provide_func_key(rambo_config_path)
@provide_config(rambo_config_path)
def _get_action(func_key, config):
    function_map = function_mapper(config, [rambo])
    return function_map[func_key]

