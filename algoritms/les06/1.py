''' 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС. '''

# Python 3.8.10, Linux 64-bit
import sys
from random import randint

def two_min_el():
    list_r = [randint(0, 99) for _ in range(100)]
    print(list_r)

    list_s = []
    list_s.extend(list_r)
    list_s.sort()

    print(f'Два наименьших элемента: {list_s[0]} и {list_s[1]}')
    
    print('Размер списка', sys.getsizeof(list_r))

    print('Размер элемента списка', sys.getsizeof(list_r[0]))
    print('Размер кортежа', sys.getsizeof(tuple(list_r)))
    print('Размер элемента кортежа', sys.getsizeof(tuple(list_r)[0]))
    sum = 0
    for size in list_r:
        sum += sys.getsizeof(size)
    print('Размер всех элементов в листе', sum)


if __name__ == '__main__':
    two_min_el()

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

    print(
        f'Два наименьших элемента (второй способ): {list_r[min_i_1]} и {list_r[min_i_2]}')

    print('Размер списка', sys.getsizeof(list_r))

    print('Размер элемента списка', sys.getsizeof(list_r[0]))
    print('Размер кортежа', sys.getsizeof(tuple(list_r)))
    print('Размер элемента кортежа', sys.getsizeof(tuple(list_r)[0]))
    sum = 0
    for size in list_r:
        sum += sys.getsizeof(size)
    print('Размер всех элементов в листе', sum)
    
if __name__ == '__main__':
    two_min_el_two()

''' 
В обоих случаях размер списка больше, чем у кортежа, с одинаковыми данными
(904 байт у списка, 840 байт у кортежа). 
Каждый элемент списка занимает 28 байт. 100 элементов по 28 байт занимают в первом варианте
2788 байт, во втором 2800 байт. Это больше размера списка этих данных, т.к. Python
делает оптимизацию и создаёт ссылки на один и тот же объект.
'''
