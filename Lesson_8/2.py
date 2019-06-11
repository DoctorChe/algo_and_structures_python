"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib
import random
import string


def cacl_hash(s, r, N, i=0):
    if i < N:
        if i == 0:
            N = len(s) - 1
        else:
            N = len(s)
        for j in range(N, i, -1):
            print(s[i:j])
            r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
        i += 1
        return cacl_hash(s, r, N, i)
    else:
        return r


length = 10
s = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
print(f"Исходная строка: {s}")

r = set()
N = len(s)
print(f"Количество различных подстрок в строке '{s}' равно {len(cacl_hash(s, r, N))}")
