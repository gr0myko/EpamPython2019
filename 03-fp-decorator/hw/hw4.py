'''
@applydecorator
def saymyname(f, *args, **kwargs):
  print('Name is', f.__name__)
  return f(*args, **kwargs)

# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever

print(*(foo(40, 2)))
foo
40 2
'''


def applydecorator(new_decorator):
    def saymyname_decorator(f):
        def wrapper(*args, **kwargs):
            return new_decorator(f, *args, **kwargs)
        return wrapper
    return saymyname_decorator


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)


@saymyname
def foo(*whatever):
    return whatever


print(*(foo(40, 2)))
