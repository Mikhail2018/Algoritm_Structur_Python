# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.


import hashlib

def count_substring_hash(s: str):
   set_hash = set()
   for i in range(len(s)):
       for j in range(i + 1, len(s) + 1):
           set_hash.add(hash(s[i:j]))
   return len(set_hash) - 1


def count_substring_sha1(s: str):
    set_sha1 = set()
    for i in range(len(s)):
       for j in range(i + 1, len(s) + 1):
          set_sha1.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    return len(set_sha1) - 1


my_str='Worldwide'

count_1 = count_substring_hash(my_str)
print(f'В строке "{my_str}"\n есть {count_1} различных подстрок')

count_2 = count_substring_sha1(my_str)
print(f'В строке "{my_str}"\n есть {count_2} различных подстрок')

