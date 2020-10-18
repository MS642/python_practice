def new_decorator(func):
    def wrap_function():
        print('This is a wrapper before the function')
        func()
        print('This is a wrapper after the function')
        print('*************')
    print('******XX******')
    return wrap_function


def new_func():
    print('Hello There')


decorated_func = new_decorator(new_func)
decorated_func()

print('===================')


@new_decorator
def ready_decorated_func():
    print('Hello I am ready')


ready_decorated_func()
