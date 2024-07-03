from functools import wraps
import time


class ControlledException(Exception):
    """A generic exception on the program's domain."""


def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        for _ in range(3):
            operation(*args, **kwargs)

    return wrapped


@retry
def add(a, b):
    return a + b


add(2, 5)


def logging_decorator(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        print("running function", function.__qualname__)
        results = function(*args, **kwargs)
        print(f"function finished: {results}")
        return results

    return wrapped


@logging_decorator
def process_account(account_id: str):
    return account_id


x = process_account("20")
print(x)


def timing_decorator(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        start = time.time()
        print(f"Function started {start}")
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Function ended {end}")
        print(f"Function took {end - start}")
        return result

    return wrapped


@timing_decorator
def check_time():
    print("hello time")


check_time()


def validation(function):
    @wraps(function)
    def wrapped(a, b):
        if a == 5:
            raise Exception("Validation Error")
        else:
            results = function(a, b)
            return results

    return wrapped


@validation
def test_function(a, b):
    return a + b


x = test_function(4, 1)
print(x)
