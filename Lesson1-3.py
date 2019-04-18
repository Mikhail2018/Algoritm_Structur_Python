# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

print('Введите координаты точки А(x, y): ')
x1 = float(input('x = '))
y1 = float(input('y = '))
print('Введите координаты точки B(x, y): ')
x2 = float(input('x = '))
y2 = float(input('y = '))

print('Уровнение прямой: ')
if x1 == x2:
    print(f'x = {x1}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    func = f'y = {k} * x + {b}'
    print(func)