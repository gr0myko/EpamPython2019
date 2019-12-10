from functools import reduce


def atom(value=None):

    def get_value():
        return value

    def set_value(new_value):
        value = new_value
        return value

    def process_value(*args):
        return reduce(lambda x, f: f(x), args, value)

    def delete_value():
        del value
    return get_value, set_value, process_value, delete_value


get_v, set_v, pr_v, del_v = atom(value=124)
