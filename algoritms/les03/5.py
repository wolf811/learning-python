# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import randint
def max_negative():
    list_r = [randint(-99, 99) for _ in range(100)]
    print(list_r)
    min_i = 0
    for i in list_r:
        if list_r[min_i] > i:
            min_i = list_r.index(i)
            
    if list_r[min_i] >= 0:
        print(f'Отрицательные элементы отсутствуют')
    else:
        print(f'Максимальный отрицательный элемент: {list_r[min_i]}. Позиция {min_i}')
if __name__ == '__main__':
    max_negative()
