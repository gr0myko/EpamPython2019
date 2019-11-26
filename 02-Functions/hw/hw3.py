counter_name = 4


def make_it_count(func, counter_name):
    def func_incremented():
        global counter_name
        counter_name += 1
        return func(counter_name)
    return func_incremented


try_fucntion = make_it_count(float, counter_name)
a = try_fucntion()
b = try_fucntion()
print(counter_name, b)
