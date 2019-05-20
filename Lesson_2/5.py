"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

# Расчёт через цикл
print("\nРасчёт через цикл")
for symbol in range(32, 128):
    print(f"{symbol}-\"{chr(symbol)}\"\t", end="")
    if (symbol - 41) % 10 == 0:
        print("\n")


# Расчёт через рекурсию
def print_ascii_table(symbol=32):
    if symbol <= 127:
        print(f"{symbol}-\"{chr(symbol)}\"\t", end="")
        symbol += 1
        if (symbol - 41) % 10 == 0:
            print("\n")
    else:
        return
    print_ascii_table(symbol)


print("\n\nРасчёт через рекурсию")
print_ascii_table()
