"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


# Расчёт через цикл
def sum_digits(number):
    result = 0
    while number:
        digit = number % 10
        result += digit
        number = int(number / 10)
    return result


# Расчёт через рекурсию
def sum_digits_recursion(number, result=0):
    if number:
        digit = number % 10
        result += digit
        return sum_digits_recursion(int(number / 10), result)
    else:
        return result


a = int(input(f"Введите первое натуральное число: "))
b = int(input(f"Введите второе натуральное число: "))


print("\nРасчёт через цикл")
sum_digits_a = sum_digits(a)
sum_digits_b = sum_digits(b)

if sum_digits_a > sum_digits_b:
    print(f"Наибольшее число по сумме цифр {a}")
    print(f"Сумма его цифр равна: {sum_digits_a}")
elif sum_digits_a < sum_digits_b:
    print(f"Наибольшее число по сумме цифр {b}")
    print(f"Сумма его цифр равна: {sum_digits_b}")
else:
    print(f"Суммы цифр введённых чисел равны")


print("\nРасчёт через рекурсию")
sum_digits_a = sum_digits_recursion(a)
sum_digits_b = sum_digits_recursion(b)
if sum_digits_a > sum_digits_b:
    print(f"Наибольшее число по сумме цифр {a}")
    print(f"Сумма его цифр равна: {sum_digits_a}")
elif sum_digits_a < sum_digits_b:
    print(f"Наибольшее число по сумме цифр {b}")
    print(f"Сумма его цифр равна: {sum_digits_b}")
else:
    print(f"Суммы цифр введённых чисел равны")
