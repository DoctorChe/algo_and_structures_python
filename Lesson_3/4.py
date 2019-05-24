# 4.	Определить, какое число в массиве встречается чаще всего.

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
max_number = 5
lst = [int(random() * max_number + 1) for _ in range(list_length)]
print(f"Исходный массив:\n{lst}\n")

unique_list = []
count_list = []
count_max = 0
count_max_index = -1

for el in lst:
    if unique_list:
        i = list_index(unique_list, el)
        if i == -1:
            unique_list.append(el)
            count_list.append(1)
        else:
            count_list[i] += 1
            if count_list[i] > count_max:
                count_max = count_list[i]
                count_max_index = i
    else:
        unique_list.append(el)
        count_list.append(1)
        count_max = 1
        count_max_index = 0

print(f"Самое часто встречающееся число масива: {unique_list[count_max_index]} встречается {count_max} раз(а)")
