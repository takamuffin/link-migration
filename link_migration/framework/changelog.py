
from functools import wraps

__all__ = [
    'changelog'
]


class ChangeLog:
    def __init__(self, output):
        self.output = output

    def record(self, *args):
        with open(self.output, "a") as write:
            write.write(','.join([f'"{str(arg)}"' for arg in args]) + '\n')


def changelog(output):
    def decorator(func):
        @wraps(func)
        def wrapper(self):
            return func(self, output=ChangeLog(self.config.MIGRATIONS_ABS_PATH + output))
        return wrapper
    return decorator
