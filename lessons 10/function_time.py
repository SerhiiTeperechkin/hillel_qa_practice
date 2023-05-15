import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} completed for {execution_time} seconds")
        return result
    return wrapper


@measure_time
def my_function():
    # Function code
    pass


my_function()
