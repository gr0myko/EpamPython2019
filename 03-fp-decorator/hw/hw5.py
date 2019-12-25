'''
Написать профилирующий декоратор.

Написать функцию-декоратор, которая подсчитывает суммарное количество вызовов декорируемой функции и общее время,
затраченное на исполнение этой функции по всем вызовам и сохраняет эти данные в глобальную переменную,
имя которой передаётся декоратору.

Проверить при помощи этой функции время исполнения различных алгоритмов поиска чисел фиббоначи.
Найти наиболее оптимальный метод.
'''
import datetime
import math

fib_results, fib2_results, fib3_results = {}, {}, {}


def prof_decorator(global_value_name: str):
    def decorator(fn):
        def calls_counter(*args, **kwargs):
            globals()[global_value_name]['calls'] += 1
            start = datetime.datetime.now()
            result = fn(*args, **kwargs)
            globals()[global_value_name]['time'] += (datetime.datetime.now() - start).microseconds
            return result
        globals()[global_value_name]['calls'] = 0
        globals()[global_value_name]['time'] = 0
        return calls_counter
    return decorator


@prof_decorator('fib_results')
def fib(n):
    """
    Recursion
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(24))
print(fib_results)  # {'calls': 92735, 'time': 6819392}


@prof_decorator('fib2_results')
def fib2(n):
    """
     Using for loop
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib2(24))
print(fib2_results)  # {'calls': 1, 'time': 0}


@prof_decorator('fib3_results')
def fib3(n):
    """
    Using formula
    """
    sqrt5 = math.sqrt(5)
    phi = (sqrt5 + 1) / 2
    return int(phi ** n / sqrt5 + 0.5)


print(fib3(24))
print(fib3_results)  # {'calls': 1, 'time': 0}

'''
Рекурсия занимает много времени, подсчет по формуле может быть неточным на больших числах, 
оптимальный - подсчет с помощью цикла for
'''
