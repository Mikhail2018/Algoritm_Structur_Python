# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

a = int(input('Введите длину отрезка А: '))
b = int(input('Введите длину отрезка B: '))
c = int(input('Введите длину отрезка C: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Такого треугольника не существует')
elif a != b and a != c and b != c:
    print('Треугольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')