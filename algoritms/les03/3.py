# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
from random import randint
def change_el():
    list_r = [randint(0, 20) for _ in range(5)]
    print(f'Массив случайных чисел: {list_r}')
    max_el_i = list_r.index(max(list_r))
    min_el_i = list_r.index(min(list_r))
    list_r[max_el_i], list_r[min_el_i] = list_r[min_el_i], list_r[max_el_i]
    print(f'Измененный массив: {list_r}')

if __name__ == '__main__':
    change_el()
