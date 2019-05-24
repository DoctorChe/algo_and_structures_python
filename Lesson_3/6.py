"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random


def list_index(lst, el):
    result = -1
    index = 0
    for lst_el in lst:
        if el == lst_el:
            result = index
            break
        index += 1
    return result


list_length = 20
max_number = 100
lst = [int(random() * max_number) for _ in range(list_length)]
print(f"Исходный массив:\n{lst}\n")

max_el = lst[0]
min_el = lst[0]

for el in lst[1:]:
    if el < min_el:
        min_el = el
    if el > max_el:
        max_el = el

max_index = list_index(lst, max_el)
min_index = list_index(lst, min_el)
sum_el = 0

if max_index > min_index:
    for i in range(min_index + 1, max_index):
        sum_el += lst[i]
else:
    for i in range(max_index + 1, min_index):
        sum_el += lst[i]

print(f"Минимальный элемент массива: {min_el} (индекс равен: {min_index})")
print(f"Максимальный элемент массива: {max_el} (индекс равен: {max_index})")
print(f"Сумма элементов, находящихся между минимальным и максимальным элементами равна: {sum_el}")
