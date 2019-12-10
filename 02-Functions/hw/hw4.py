import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):
    def new_func(*new_args, **new_kwargs):
        if not new_args and not new_kwargs:
            return func(fixated_args, fixated_kwargs)
        else:
            all_args = fixated_args + new_args
            fixated_kwargs.update(new_kwargs)
            return func(all_args, fixated_kwargs)
    new_func.__name__ = f'func_{func}'
    new_func.__doc__ = f""" 
    A func implementation of {new_func.__name__} 
    with pre-applied arguments being: 
    {inspect.getargvalues(inspect.currentframe()).locals['fixated_args']},
    {inspect.getargvalues(inspect.currentframe()).locals['fixated_kwargs']}
    source_code: 
    {inspect.getsource(new_func)}
    """
    return new_func


try_function = modified_func(print, 5, 10, val1=17, val2=20)
try_function(1, val3=3)
print(try_function.__name__)
print(try_function.__doc__)
