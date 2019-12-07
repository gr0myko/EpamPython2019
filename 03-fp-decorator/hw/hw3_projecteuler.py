def self_powers_sum_last_10_digits(numbers_count):
    result = sum(i**i for i in range(1, numbers_count+1)) % 10**10
    return result


print(self_powers_sum_last_10_digits(1000))
