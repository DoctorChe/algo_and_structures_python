"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


# Расчёт через цикл
def sum_range(n):
    sum_range_n = 0
    for i in range(1, n + 1):
        sum_range_n += i
    return sum_range_n


# Расчёт через рекурсию
def sum_range_recursion(n, i=1, sum_range_n=0):
    if i < n:
        sum_range_n += i
        i += 1
        return sum_range_recursion(n, i, sum_range_n)
    else:
        return sum_range_n + n


n = int(input(f"Введите натуральное число: "))
sum_n = int(n * (n + 1) / 2)

print("\nРасчёт через цикл")
sum_range_n = sum_range(n)
if sum_range_n == sum_n:
    print(f"1+2+...+{n} = {sum_range_n}")
    print(f"n(n+1)/2 = {sum_n}")
    print(f"1+2+...+{n} = n(n+1)/2")
else:
    print(f"1+2+...+{n} = {sum_range_n}")
    print(f"n(n+1)/2 = {sum_n}")
    print(f"1+2+...+{n} <> n(n+1)/2")


print("\n\nРасчёт через рекурсию")
sum_range_n = sum_range_recursion(n)
if sum_range_n == sum_n:
    print(f"1+2+...+{n} = {sum_range_n}")
    print(f"n(n+1)/2 = {sum_n}")
    print(f"1+2+...+{n} = n(n+1)/2")
else:
    print(f"1+2+...+{n} = {sum_range_n}")
    print(f"n(n+1)/2 = {sum_n}")
    print(f"1+2+...+{n} <> n(n+1)/2")
