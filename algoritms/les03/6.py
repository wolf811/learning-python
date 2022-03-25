# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
from random import randint
def sum_min_max():
    list_r = [randint(0, 99) for _ in range(10)]
    print(list_r)

    min_i = 0
    max_i = 0
    step = 1
    sum = 0

    for i in list_r:
        if list_r[min_i] > i:
            min_i = list_r.index(i)
        elif list_r[max_i] < i:
            max_i = list_r.index(i)

    if max_i - min_i < 0:
        step = -1

    for i in list_r[min_i + step:max_i:step]:
        sum += i

    print(f'Сумма между мин. ({list_r[min_i]}) и макс. ({list_r[max_i]}) элементами: {sum}')
    
if __name__ == '__main__':
    sum_min_max()
