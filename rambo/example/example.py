from rambo.example.actions import get_action

if __name__ == "__main__":
    """ the get action function will return the function 
    to execute based on the command line values"""
    action = get_action()
    action()
