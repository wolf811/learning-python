''' 1. Определение количества различных подстрок с использованием хэш-функции. 
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. 
Требуется найти количество различных подстрок в этой строке. '''

import hashlib
def number_substrings():
    string = input('Введите строку из маленьких латинских букв: ')

    sum_substring = set()

    for i in range(len(string)):
        for j in range(len(string), i, -1):
            hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)

    print(f'{len(sum_substring) -1} подстрок в строке {string}')

if __name__ == "__main__":
    number_substrings()