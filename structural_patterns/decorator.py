from functools import wraps
def decorator_func(func):
    @wraps(func)
    def wrapper_func(*args):
        # Increments the args by 10
        return func(*([arg+10 for arg in list(args)]))
    return wrapper_func

@decorator_func
def print_args(*args):
    print(args)

print_args(10,20,30)