"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import timeit
import cProfile

n = 1


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
    return primes


print(timeit.timeit("eratosthenes(n)",
                    setup="from __main__ import eratosthenes, n",
                    number=1000))

print(timeit.timeit("search_primes(n)",
                    setup="from __main__ import search_primes, is_prime, n",
                    number=1000))


def main():
    print(f"{n}-e простое число: {eratosthenes(n)[-1]} (Решето Эратосфена)")
    print(f"{n}-e простое число: {search_primes(n)[-1]}")


cProfile.run("main()")

"""
Согласно замерам скорости алгоритмов практически равны

Вариант 1 (Решето Эратосфена)
1       0.5323531484536379
10      1.1358938288516052
100     1.5968808650130994
1000    3.6435655995407545

Вариант 2
1       0.0002637652263693946
10      0.01717826629271979
100     0.4012091463243581
1000    8.843595431353647

"""