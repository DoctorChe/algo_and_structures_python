"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import randint


def merge_sort(a):
    n = len(a)
    if n < 2:
        return a
    left = merge_sort(a[:n//2])
    right = merge_sort(a[n//2:n])
    i = j = 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res


lst = [randint(0, 50) for i in range(20)]
print(lst)
print(merge_sort(lst))
