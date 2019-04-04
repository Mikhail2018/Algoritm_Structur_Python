# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import timeit
from itertools import product


def n_number():
    a = [0] * 8
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                a[j - 2] += 1
    i = 0
    while i < len(a):
        print(i + 2, ' - ', a[i])
        i += 1

def n_number_opt():
    a = [0, 1,2,3,4,5,6,7]
    for i, j in product(range(2, 100), range(2, 10)):
        if i % j == 0:
            a[j-2] += 1
    i = 0
    while i < len(a):
        print(i + 2, ' - ', a[i])
        i += 1


one = timeit.timeit('n_number()', setup='from __main__ import n_number', number=100000)
two = timeit.timeit('n_number_opt()', setup='from __main__ import n_number_opt', number=100000)
print(one,  ' ', two)