"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# from pympler
import sys
# import timeit
# import cProfile

n = 10


# Вариант 1 (Решето Эратосфена)
def eratosthenes(n):
    max_number = 10000
    a = list(range(max_number + 1))
    a[1] = 0
    primes = []

    i = 2
    while len(primes) < n:
        if a[i] != 0:
            primes.append(a[i])
            for j in range(i, max_number + 1, i):
                a[j] = 0
        i += 1
    print(sys.getrefcount(1))
    return primes


# Вариант 2
def is_prime(n):
    for j in range(3, int(n ** 0.5) + 1):
        if n % j == 0:
            return 0
    return 1


def search_primes(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i) == 1:
            primes.append(i)
        i += 2
    print(sys.getrefcount(1))
    return primes


# print(timeit.timeit("eratosthenes(n)",
#                     setup="from __main__ import eratosthenes, n",
#                     number=1000))
#
#
# print(timeit.timeit("search_primes(n)",
#                     setup="from __main__ import search_primes, is_prime, n",
#                     number=1000))


def main():
    # print(f"{n}-e простое число: {eratosthenes(n)[-1]} (Решето Эратосфена)")
    print(f"{n}-e простое число: {search_primes(n)[-1]}")


# cProfile.run("main()")

main()

"""
Python 3.6
x64
"""
