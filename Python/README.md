
## Index

2. [Import](#002_import)
1. [Timeit_wrapper](#001_Timeit_wrapper)

<hr>

# 002_import
```python
import importlib
import util
importlib.reload(util)
from util import *
```

# 001_Timeit_wrapper

To time the function being executed.

*source: [Making Python Programs Blazingly Fast](https://martinheinz.dev/blog/13) (Martin, 2020-01-01T20:00:00Z)

```python
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
```


2. Python 2 to 3


- print => print()

- 'dict' object has no attribute 'iteritems'
```python
dict.iteritems()
dict.items()
```

- izip => zip
```python
try:
    # Python 2
    from itertools import izip
except ImportError:
    # Python 3
    izip = zip
```

- 'str' object has no attribute 'decode'
```python
str.decode("utf8")
str
```

- name 'xrange' is not defined
```python
name 'xrange' is not defined
range
```
