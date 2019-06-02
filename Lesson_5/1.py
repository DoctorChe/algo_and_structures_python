"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import OrderedDict


def avg(lst):
    return sum(lst) / len(lst)

# d = {}
# n = int(input("Введите количество предприятий: "))
# for i in range(n):
#     name = input(f"Введите наименование {i+1}-го предприятия: ")
#     d[name] = []
#     for j in range(4):
#         profit = int(input(f"Введите прибыль {i+1}-го предприятия за {j+1} квартал: "))
#         d[name].append(profit)


d = {
    "q": [1, 2, 3, 4],
    "w": [2, 3, 4, 5],
    "e": [3, 4, 5, 6],
    "r": [4, 5, 6, 7],
    "t": [5, 6, 7, 8],
    "y": [6, 7, 8, 9],
}

avg_profit = avg([avg(d[i]) for i in d])

less_avg = {}
more_avg = {}

for k, v in d.items():
    if avg(v) < avg_profit:
        less_avg[k] = avg(v)
    elif avg(v) > avg_profit:
        more_avg[k] = avg(v)

less_avg = OrderedDict(sorted(less_avg.items()))
more_avg = OrderedDict(sorted(more_avg.items()))

print(f"Средняя прибыль за год для всех предприятий: {avg_profit}")
print("Предприятия, чья прибыль выше среднего:")
for k, v in more_avg.items():
    print(f"Название предприятия: {k}, средняя прибыль за год: {v}")
print("Предприятия, чья прибыль ниже среднего:")
for k, v in less_avg.items():
    print(f"Название предприятия: {k}, средняя прибыль за год: {v}")
