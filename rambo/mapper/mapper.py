
def get_function_names(config: dict) -> list:
    actions = config["commands"]["action"]["choices"]
    objects = config["commands"]["object"]["choices"]
    return [f"{a}_{o}" for a in actions for o in objects]


def function_mapper(config: dict, modules: list) -> dict:
    mapped_functions = {}
    functions = get_function_names(config)
    for module in modules:
        for function in functions:
            func = getattr(module, function, None)
            if func:
                mapped_functions[function] = func
    return mapped_functions
