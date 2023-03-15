### Example 

import functools
def add_attrs(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*vars, **kwargs):
            l=[i for i in vars]
            l.extend(kwargs.values())
            n_l=[type(i) for i in l]
            arg=[i for i in args]
            if not set(n_l).issubset(set(arg)):
                raise TypeError
            return func(*vars,**kwargs)
        return wrapper
    return decorator

#Decorator timer

import functools, time

def timer(iters=1):
    def decorator(func):   
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.perf_counter()
                value = func(*args, **kwargs)
                end = time.perf_counter()
                total += end - start
            print(f'Среднее время выполнения {func.__name__}: {round(total/iters, 4)} сек.')
            return value
        return wrapper
    return decorator

