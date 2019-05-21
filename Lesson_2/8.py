"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


# Расчёт через цикл
def count_digit(number, my_digit):
    count = 0
    while number:
        digit = number % 10
        if my_digit == digit:
            count += 1
        number = int(number / 10)
    return count


def loop(n, my_digit):
    total_count = 0
    for i in range(1, n + 1):
        number = int(input(f"Введите {i}-е число: "))
        total_count += count_digit(number, my_digit)
    return total_count


# Расчёт через рекурсию
def count_digit_recursion(number, my_digit, count=0):
    if number:
        digit = number % 10
        if my_digit == digit:
            count += 1
        return count_digit_recursion(int(number / 10), my_digit, count)
    else:
        return count


def recursion(n, my_digit, i=1, total_count=0):
    if i <= n:
        number = int(input(f"Введите {i}-е число: "))
        total_count += count_digit_recursion(number, my_digit)
        i += 1
        return recursion(n, my_digit, i, total_count)
    else:
        return total_count


n = int(input(f"Введите колличество вводимых чисел: "))
my_digit = int(input(f"Введите цифру, которую будем искать: "))

print("\nРасчёт через цикл")
print(f"Цифра {my_digit} встречается {loop(n, my_digit)} раз(а)")

print("\nРасчёт через рекурсию")
print(f"Цифра {my_digit} встречается {recursion(n, my_digit)} раз(а)")
