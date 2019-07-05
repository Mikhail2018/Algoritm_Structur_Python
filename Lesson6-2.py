# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.

import sys

n = int(input('Введите число: '))
s = 0
for i in range(1,n + 1):
    s += i
m = n * (n + 1) // 2
print(s)
print(m)

print('Программой было использовано памяти: %d байт' % (sys.getsizeof(n) + sys.getsizeof(s) + sys.getsizeof(i)
                                                        + sys.getsizeof(m)))

# При изминении числа ввода использованной памяти становиться больше
# Операционная система MacOS 64bit