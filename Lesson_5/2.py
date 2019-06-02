"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

ABC = "0123456789ABCDEF"


def get_10_digits(lst, max_len_lst):
    result = deque()
    for i in range(max_len_lst):
        try:
            digit_hex_a = lst[-(i+1)]
            digit_a = ABC.index(digit_hex_a)
        except IndexError:
            digit_a = 0
        result.appendleft(digit_a)
    return result


def sum_hex(a_hex, b_hex):
    max_len = max(len(a_hex), len(b_hex))
    a_10 = get_10_digits(a_hex, max_len)
    b_10 = get_10_digits(b_hex, max_len)
    result = deque()
    transfer = 0
    for i in range(max_len):
        d1 = a_10[-(i + 1)]
        d2 = b_10[-(i + 1)]
        sum_d = (d1 + d2 + transfer) % 16
        transfer = (d1 + d2 + transfer) // 16
        result.appendleft(ABC[sum_d])
    if transfer:
        result.appendleft(ABC[transfer])
    return list(result)


def pow_hex(a_hex, b_hex):
    pows_1 = []
    for i in range(len(b_hex)):
        pow_1 = pow_hex_1(a_hex, b_hex[-(i+1)])
        for _ in range(i):
            pow_1.append("0")
        pows_1.insert(0, pow_1)
    result = pows_1[0]
    for i in range(1, len(pows_1)):
        result = sum_hex(result, pows_1[i])
    return result


def pow_hex_1(num_hex, dig_hex):
    num_10 = get_10_digits(num_hex, len(num_hex))
    dig_10 = ABC.index(dig_hex)
    result = []
    transfer = 0
    for i in reversed(num_10):
        pow_d = (i * dig_10 + transfer) % 16
        transfer = (i * dig_10 + transfer) // 16
        result.insert(0, ABC[pow_d])
    if transfer:
        result.insert(0, ABC[transfer % 16])
        if transfer // 16:
            result.insert(0, ABC[transfer // 16])
    return result


# a = list(input("Введите первое шестнадцатеричное число: "))
# b = list(input("Введите второе шестнадцатеричное число: "))

a = list("A2")
b = list("C4F")

print(f"{a} + {b} = {sum_hex(a, b)}")
print(f"{a} * {b} = {pow_hex(a, b)}")
