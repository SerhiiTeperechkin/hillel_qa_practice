# 3. Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000, і повертає True,
# якщо це просте число, і False в іншому випадку.

def is_prime(number):
    if number < 2 or number > 1000:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
