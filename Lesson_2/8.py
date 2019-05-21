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


# Расчёт через рекурсию
def count_digit_recursion(number, my_digit, count=0):
    if number:
        digit = number % 10
        if my_digit == digit:
            count += 1
        return count_digit_recursion(int(number / 10), my_digit, count)
    else:
        return count


input_number = int(input(f"Введите последовательность чисел: "))
my_digit = int(input(f"Введите цифру: "))

print("\nРасчёт через цикл")
print(f"Цифра {my_digit} встречается {count_digit(input_number, my_digit)} раз(а)")

print("\nРасчёт через рекурсию")
print(f"Цифра {my_digit} встречается {count_digit_recursion(input_number, my_digit)} раз(а)")
