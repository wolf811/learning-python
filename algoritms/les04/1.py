# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
import timeit 
from random import randint

# Первая реализация
def two_min_el_one():
    list_r = [randint(0, 99) for _ in range(100)]
    print(list_r)

    list_s = []
    list_s.extend(list_r)
    list_s.sort()

    print(f'Два наименьших элемента: {list_s[0]} и {list_s[1]}')

if __name__ == '__main__':
    # two_min_el_one()
    print(timeit.timeit(two_min_el_one, number=3))
    

# Вторая реализация
def two_min_el_two():
    list_r = [randint(0, 99) for _ in range(100)]
    print(list_r)

    min_i_1 = 0
    min_i_2 = 1

    for i in list_r:
        if list_r[min_i_1] > i:
            min_i_2 = min_i_1
            min_i_1 = list_r.index(i)
        elif list_r[min_i_2] > i:
            min_i_2 = list_r.index(i)

    print(f'Два наименьших элемента (второй способ): {list_r[min_i_1]} и {list_r[min_i_2]}')

if __name__ == '__main__':
    # two_min_el_two()
    print(timeit.timeit(two_min_el_two, number=3))

''' Скорость выполнения 1-го способа 0.012080648999472032 сек, 2-го 0.0046378939996429835 сек, т.е. второй способ немного быстрей. Сложность линейная. '''
