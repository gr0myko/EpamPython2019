try_variable = 4


def make_it_count(func, counter_name):
    def func_incremented():
        global global_counter_name
        global_counter_name = counter_name
        global_counter_name += 1
        return func(counter_name)
    return func_incremented


try_fucntion = make_it_count(float, try_variable)
a = try_fucntion()
b = try_fucntion()
print(try_variable, b)
