"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


# Расчёт через цикл
def sum_range_n(n):
    number = -2
    sum_n = 0
    for i in range(n):
        number = number / 2 * -1
        sum_n += number
    return sum_n


# Расчёт через рекурсию
def sum_range_n_recursion(n, i=0, number=-2.0, sum_n=0):
    if i >= n:
        return sum_n
    number = number / 2 * -1
    sum_n += number
    i += 1
    return sum_range_n_recursion(n, i, number, sum_n)


n = int(input("Введите количество элементов: "))

print("\nРасчёт через цикл")
print(f"Сумма {n} чисел из ряда 1 -0.5 0.25 -0.125 ... равна {sum_range_n(n)}")

print("\nРасчёт через рекурсию")
print(f"Сумма {n} чисел из ряда 1 -0.5 0.25 -0.125 ... равна {sum_range_n_recursion(n)}")
