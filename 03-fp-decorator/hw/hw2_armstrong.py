def is_armstrong(number):
    sum_of_digits = sum(int(i)**len(str(number)) for i in str(number))
    if sum_of_digits == number:
        return True
    elif sum_of_digits != number:
        return False


assert is_armstrong(153) == True, 'Число Армстронга'
assert is_armstrong(10) == False, 'Не число Армстронга'
