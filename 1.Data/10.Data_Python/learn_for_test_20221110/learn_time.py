import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        rval = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Executed in {duration:.4f} seconds")
        return rval
    return wrapper

@timer
def execution_fn():
    for i in range(3):
        time.sleep(1)

execution_fn()

