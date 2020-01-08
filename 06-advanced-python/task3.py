""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception_value, traceback):
        return isinstance(exception_value, self.exception)


with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")

