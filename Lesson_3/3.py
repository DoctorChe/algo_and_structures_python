# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random

n = 20
lst = [0] * n
for i in range(n):
    lst[i] = int(random()*100)
# lst = [int(random()*100) for _ in range(n)]
print(f"Исходный массив:\n{lst}\n")

min_number = lst[0]
max_number = lst[0]
min_index = 0
max_index = 0

for i in range(1, n):
    if lst[i] < min_number:
        min_number = lst[i]
        min_index = i
    if lst[i] > max_number:
        max_number = lst[i]
        max_index = i

print(f"Минимальный элемент массива:{min_number}")
print(f"Максимальный элемент массива:{max_number}")

lst[min_index], lst[max_index] = lst[max_index], lst[min_index]

print(f"\nМассив с поменяными элементами:\n{lst}")
