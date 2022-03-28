# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import randint

def two_min_el():
    list_r = [randint(0, 99) for _ in range(100)]
    print(list_r)

    list_s = []
    list_s.extend(list_r)
    list_s.sort()

    print(f'Два наименьших элемента: {list_s[0]} и {list_s[1]}')

if __name__ == '__main__':
    two_min_el()
