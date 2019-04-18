# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

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
    a = [random.randint(0,8) for _ in range(50)]

    print(a)
    a = merge(a)
    print(a)