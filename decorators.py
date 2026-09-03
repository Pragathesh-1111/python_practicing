def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('Start')
        func(*args, *kwargs)
        print('End')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


hello('Hiiiiiiiii', ':)')

from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"It took {t2-t1}s")
    return wrap_func

@performance
def long_time():
    for item in range(60000000):
        item+1

long_time()

