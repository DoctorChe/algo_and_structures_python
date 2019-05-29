"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import random
import timeit
import cProfile

list_length = 1000
max_number = 1000
lst = [int(int(random() * max_number) - (max_number / 2)) for _ in range(list_length)]


# Вариант 1
def list_index(lst, el):
    result = -1
    index = 0
    for lst_el in lst:
        if el == lst_el:
            result = index
            break
        index += 1
    return result


def fun_max_neg(max_number):
    max_negative = -max_number
    for el in lst:
        if max_negative < el < 0:
            max_negative = el
    return max_negative


print(timeit.timeit("fun_max_neg(max_number)",
                    setup="from __main__ import fun_max_neg, list_index, list_length, max_number, lst",
                    number=10000))

# Вариант 2
print(timeit.timeit("max(i for i in lst if i < 0)",
                    setup="from __main__ import lst",
                    number=10000))


def main():
    fun_max_neg(max_number)
    max(i for i in lst if i < 0)


cProfile.run("main()")

"""
Согласно замерам скорости первый алгоритм получился быстрее

Вариант 1
0.6291005913677955

Вариант 2
0.7705054371215858

Увеличение времени второго варианта происходит вероятно из-за многократного вызова генераторного выражения 
"""