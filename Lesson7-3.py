
import random
import sys
import timeit

# Сортировка пузырьком
def bubble_sort(sort_arr):
    a = sort_arr

    for k in range(len(a)-1, 0, -1):
        for i in range(k):
            if a[i] < a[i + 1]:
                a[i], a[i + 1 ] = a[i + 1], a[i]
        return a

# Сортировка слиянием
def merge(a):
    n = len(a)
    if n <= 1:
        return a

    l = merge(a[:n // 2])
    r = merge(a[n // 2 :])

    i, j = 0, 0
    while i < len(l) or j < len(r):
        if not i < len(l):
            a[i + j] = r[j]
            j += 1
        elif not j < len(r):
            a[i + j] = l[i]
            i += 1
        elif l[i] < r[j]:
            a[i + j] = l[i]
            i += 1
        else:
            a[i + j] = r[j]
            j += 1
    return a

if __name__ == '__main__':
    numbers = []
    for n in range(-100, 100):
        numbers.append(n)

    a = [random.randint(0,8) for _ in range(50)]

    bubble = timeit.timeit('bubble_sort(numbers)', setup='from __main__ import bubble_sort, numbers', number=1)
    merges = timeit.timeit('merge(a)', setup='from __main__ import merge, a', number=1)
    print()
    print(f'Сортировка пузырьковым методом выполнена за {bubble}')
    print(f'Сортировка методом слитяния выполнена за {merges}')