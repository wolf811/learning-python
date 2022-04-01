# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

import math
import timeit

def not_sieve_eratosthenes(i):
    '''Функция поиска i-го простого числа,
    без использования алгоритма «Решето Эратосфена»
    '''
    lst_prime = [2]
    num = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if num % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(num)
        num += 1
    return lst_prime[-1]


def sieve_eratosthenes(i):
    '''Функция поиска i-го простого числа,
    используя алгоритм «Решето Эратосфена»
    '''
    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for num in lst_prime:
        if lst_prime.index(num) <= num - 1:
            for j in range(2, len(lst_prime)):
                if num * j in lst_prime[num:]:
                    lst_prime.remove(num * j)
        else:
            break
    return lst_prime[i - 1]

def prime_counting_function(i):
    '''Функция возвращает верхнюю границу отрезка на котором лежат
    i-e количество простых чисел. Функция основана на теореме о
    распределении простых чисел, она утверждает, что функция
    распределения простых чисел. Количество простых чисел на отрезке
    [1;n] растёт с увеличением n как n / ln(n).
    '''
    num_of_primes = 0
    num = 2
    while num_of_primes <= i:
        num_of_primes = num / math.log(num)
        num += 1
    return num


NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

time1 = timeit.timeit(f'not_sieve_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import not_sieve_eratosthenes',
                      number=NUMBER_EXECUTIONS)

time2 = timeit.timeit(f'sieve_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import sieve_eratosthenes',
                      number=NUMBER_EXECUTIONS)

print(f'Программа без использования алгоритма «Решето Эратосфена» быстрее \
программы с использованием алгоритма «Решето Эратосфена» в \
{round(time2 / time1, 2)} раз'
      )
'''Программа без использования алгоритма «Решето Эратосфена» быстрее
программы с использованием алгоритма «Решето Эратосфена» в 72.28 раз
'''
