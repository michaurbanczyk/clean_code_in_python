# There are recurrent situations in which we want to run some code that has preconditions and postconditions,
# meaning that we want to run things before and after a certain main action, respectively.
# Most of the time, we see context managers around resource management. For example, in situations when we open files,
# we want to make sure that they are closed after processing (so we do not leak file descriptors).
# Or, if we open a connection to a service (or even a socket), we also want to be sure to close it accordingly,
# or when dealing with temporary files, and so on.
import contextlib


def stop_database():
    print("stop database")


def start_database():
    print("start database")


def db_backup():
    print("creating db backup")


# 1. First way of implementing context managers:
class DatabaseHandler:
    def __enter__(self):
        stop_database()
        return self  # this is a good practice to always try to return something on return

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_database()


def db_handler_from_class():
    with DatabaseHandler():
        db_backup()


# 2. Create a context manager from context lib
@contextlib.contextmanager
def db_handler():
    try:
        stop_database()
        yield
    finally:
        start_database()


def db_handler_from_decorator():
    with db_handler():
        db_backup()


db_handler_from_class()
db_handler_from_decorator()
