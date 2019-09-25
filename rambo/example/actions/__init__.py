from rambo import function_mapper, provide_func_key, provide_config
from rambo.example.my_app import my_app


@provide_func_key()
@provide_config()
def get_action(func_key, config):
    """
        the function mapper will map all functions in the provided module to the command line arguments
    """
    function_map = function_mapper(config, [my_app])

    if func_key in function_map.keys():
        return function_map[func_key]
    else:
        raise NotImplemented
