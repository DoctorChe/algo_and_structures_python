"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random


list_length = 10
max_number = 20
lst = [int(random() * max_number) for _ in range(list_length)]
print(f"Исходный массив:\n{lst}\n")

min_number1 = lst[0]
min_index1 = 0

for i in range(1, list_length):
    if lst[i] < min_number1:
        min_number1 = lst[i]
        min_index1 = i

if min_index1 == 0:
    min_number2 = lst[1]
    min_index2 = 1
else:
    min_number2 = lst[0]
    min_index2 = 0

for i in range(1, list_length):
    if i == min_index1 or i == min_index2:
        continue
    if lst[i] < min_number2:
        min_number2 = lst[i]
        min_index2 = i

print(f"Первый наименьший элемент массива:{min_number1}. Индекс элемента: {min_index1}")
print(f"Второй наименьший элемент массива:{min_number2}. Индекс элемента: {min_index2}")
