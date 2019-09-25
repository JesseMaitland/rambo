from rambo import provide_cmd_args, provide_config

""" this function has access to the passed in command line arguments"""
@provide_cmd_args()
def create_project(cmd_args):
    print("This function is executed when create args is passed.")
    print(cmd_args)


# will be mapped when "create file" is passed to your terminal app
def create_file():
    print("you dont have to provide cmd args if you dont need them")
    print("this function is run when create file is passed")


@provide_config()
def view_log(config):
    print(config)
    print("this function will run when we pass view log")

