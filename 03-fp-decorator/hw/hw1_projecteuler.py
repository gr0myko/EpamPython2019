def sum_square_diff(numbers_count: int):
    result = sum(range(1, numbers_count+1)) ** 2 - sum(x ** 2 for x in range(1, numbers_count+1))
    return result


print(sum_square_diff(100))
