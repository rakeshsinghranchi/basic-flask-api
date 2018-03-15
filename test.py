def deco(some_function):
    def wrapper():
        print("Something is called.")
        some_function()
        print("Something else.")
    return wrapper

def just_some_function():
    print("Wheee!")

just_some_function = deco(just_some_function)
just_some_function()
