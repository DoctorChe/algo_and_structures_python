# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

rows = 5
cols = 4
max_number = 10

m = [[int(random() * max_number) for j in range(cols)] for i in range(rows)]

print(f"Исходная матрица:")
for i in range(rows):
    for j in range(cols):
        print(m[i][j], end=" ")
    print()

for j in range(cols):
    min_col = m[0][j]
    for i in range(1, rows):
        if m[i][j] < min_col:
            min_col = m[i][j]
    if j == 0:
        max_mins = min_col
    else:
        if max_mins < min_col:
            max_mins = min_col

print(f"Максимальный элемент среди минимальных элементов столбцов матрицы равен {max_mins}")
