# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

a = 5
b = 6
a_bit = f'{a} = {bin(a)}'
b_bit = f'{b} = {bin(b)}'
and_bit = f'{a} and {b} = {a & b} ({bin(a & b)})'
or_bit = f'{a} or {b} = {a | b} ({bin(a | b)})'
xor_bit = f'{a} xor {b} = {a ^ b} ({bin(a ^ b)})'
right = f'{a} >> 3 = {a >> 3} ({bin(a >> 3)})'
left = f'{a} << 3 = {a << 3} ({bin(a << 3)})'
not_bit = f'not {a} = {~a} ({bin(~a)})'
print('\n', a_bit,
      '\n', b_bit,
      '\n', and_bit,
      '\n', or_bit,
      '\n', xor_bit,
      '\n', right,
      '\n', left,
      '\n', not_bit)