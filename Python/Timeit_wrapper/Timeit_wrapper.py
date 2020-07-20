from functools import wraps
import time
def timeit_wrapper(func):
    # https://martinheinz.dev/blog/13
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Alternatively, you can use time.process_time()
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print('{0:<10}.{1:<8} : {2:<8}'.format(func.__module__, func.__name__, end - start))
        return func_return_val
    return wrapper

@timeit_wrapper
def test_word(hobj, word):
    return 1

test_word("", 'hydroxychloroquine')

