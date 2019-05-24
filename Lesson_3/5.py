# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

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
max_number = 20
lst = [int(int(random() * max_number) - (max_number / 2)) for _ in range(list_length)]
print(f"Исходный массив:\n{lst}\n")

max_negative = -max_number
for el in lst:
    if max_negative < el < 0:
        max_negative = el

print(f"Максимальный отрицатальный элемент в массиве: {max_negative}, его позиция {list_index(lst, max_negative) + 1}")
