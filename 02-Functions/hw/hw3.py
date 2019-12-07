try_variable = 4


def make_it_count(func, counter_name: str):
    def change_global_with_func():
        value_change = globals()[counter_name]
        value_change += 1
        globals()[counter_name] = value_change
        return func(value_change)
    return change_global_with_func


try_function = make_it_count(float, 'try_variable')
a = try_function()
b = try_function()
c = try_function()
print(try_variable, c)

