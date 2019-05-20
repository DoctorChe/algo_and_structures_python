"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

input_number = int(input("Введите натуральное число: "))


# Расчёт через цикл
print("\nРасчёт через цикл")
number = input_number
even = 0
odd = 0
while number:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = int(number / 10)
print(f"В введённом числе {even} чётных цифр(ы) и {odd} нечётных цифр(ы)")


# Расчёт через рекурсию
def even_odd(number, even=0, odd=0):
    if number == 0:
        print(f"В введённом числе {even} чётных цифр(ы) и {odd} нечётных цифр(ы)")
        return
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    even_odd(int(number / 10), even, odd)


print("\nРасчёт через рекурсию")
even_odd(input_number)
