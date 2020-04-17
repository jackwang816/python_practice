# 1. simple decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
# @my_decorator is a syntax suger
@my_decorator # same as say_whee = my_decorator(say_whee)
def say_whee():
    print("Whee!")

# 2. decoratored functions with arguement and return values
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@do_twice
def say_hellow(name):
    print('hellow %s' % name)

# 3. preserve information about the original function
import functools
def do_twice_new(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

