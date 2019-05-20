"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from random import random


# Расчёт через цикл
def guess_number(rand_number, min_number, max_number):
    for i in range(10):
        number = int(input(f"Введите натуральное от {min_number} до {max_number}: "))
        if number == rand_number:
            print("Вы угадали")
            break
        elif number < rand_number:
            print("Ваше число меньше загаданного")
            min_number = number
        elif number > rand_number:
            print("Ваше число больше загаданного")
            max_number = number
    else:
        print(f"Загаданное число {rand_number}")


# Расчёт через рекурсию
def guess_number_recursion(rand_number, i=1, min_number=0, max_number=100):
    number = int(input(f"Введите натуральное от {min_number} до {max_number}: "))
    if i <= 10:
        if number == rand_number:
            print("Вы угадали")
            return
        elif number < rand_number:
            print("Ваше число меньше загаданного")
            min_number = number
        elif number > rand_number:
            print("Ваше число больше загаданного")
            max_number = number
        i += 1
    else:
        print(f"Загаданное число {rand_number}")
        return
    guess_number_recursion(rand_number, i, min_number, max_number)


min_number = 0
max_number = 100


print("\nРасчёт через цикл")
rand_number = int(random() * max_number + 1)
guess_number(rand_number, min_number, max_number)


print("\nРасчёт через рекурсию")
rand_number = int(random() * max_number + 1)
guess_number_recursion(rand_number)
