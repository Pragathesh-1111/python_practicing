def my_decorator(func):
    def wrap_func():
        print('Start')
        func()
        print('End')
    return wrap_func


@my_decorator
def hello():
    print('Helloooooo')


hello()
