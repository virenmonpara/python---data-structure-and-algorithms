def entry_exit(func):
    def wrapped_func():
        print(f"entering {func.__name__}")
        func()
        print(f"exiting {func.__name__}")
    return wrapped_func


@entry_exit
def my_func():
    print("inside my_func")


# we can use this same if we dont watn to use @entry_exit
my_func = entry_exit(my_func)


my_func()
