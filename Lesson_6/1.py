"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile

n = 100


# Вариант 1 (Решето Эратосфена)
@profile
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


@profile
def search_primes(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i) == 1:
            primes.append(i)
        i += 2
    return primes


def main():
    print(f"{n}-e простое число: {eratosthenes(n)[-1]} (Решето Эратосфена)")
    print(f"{n}-e простое число: {search_primes(n)[-1]}")


main()

"""
Python 3.6
x64

Filename: C:/Program1/PythonProjects/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    19     62.7 MiB     62.7 MiB   @profile
    20                             def eratosthenes(n):
    21     62.7 MiB      0.0 MiB       max_number = 10000
    22     62.9 MiB      0.3 MiB       a = list(range(max_number + 1))
    23     63.0 MiB      0.0 MiB       a[1] = 0
    24     63.0 MiB      0.0 MiB       primes = []
    25                             
    26     63.0 MiB      0.0 MiB       i = 2
    27     63.0 MiB      0.0 MiB       while len(primes) < n:
    28     63.0 MiB      0.0 MiB           if a[i] != 0:
    29     63.0 MiB      0.0 MiB               primes.append(a[i])
    30     63.0 MiB      0.0 MiB               for j in range(i, max_number + 1, i):
    31     63.0 MiB      0.0 MiB                   a[j] = 0
    32     63.0 MiB      0.0 MiB           i += 1
    33     63.0 MiB      0.0 MiB       return primes


100-e простое число: 541 (Решето Эратосфена)


Filename: C:/Program1/PythonProjects/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    44     62.9 MiB     62.9 MiB   @profile
    45                             def search_primes(n):
    46     62.9 MiB      0.0 MiB       primes = [2]
    47     62.9 MiB      0.0 MiB       i = 3
    48     62.9 MiB      0.0 MiB       while len(primes) < n:
    49     62.9 MiB      0.0 MiB           if is_prime(i) == 1:
    50     62.9 MiB      0.0 MiB               primes.append(i)
    51     62.9 MiB      0.0 MiB           i += 2
    52     62.9 MiB      0.0 MiB       return primes


100-e простое число: 541
"""
