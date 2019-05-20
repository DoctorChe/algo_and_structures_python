"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


# Расчёт через цикл
def revers_recursion(number):
    revers = 0
    while number / 10 > 0:
        digit = number % 10
        revers = revers * 10 + digit
        number = int(number / 10)
    return revers


# Расчёт через рекурсию
def revers_recursion(number, revers_number=0):
    if number == 0:
        return revers_number
    digit = number % 10
    revers_number = revers_number * 10 + digit
    return revers_recursion(int(number / 10), revers_number)


number = int(input("Введите натуральное число: "))

print("\nРасчёт через цикл")
print(f"Обратное число {revers_recursion(number)}")

print("\nРасчёт через рекурсию")
print(f"Обратное число {revers_recursion(number)}")
