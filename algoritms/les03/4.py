# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint
def frequent_number():
    list_r = [randint(0, 99) for _ in range(100)]
    max_i = 0
    for i in list_r:
        if list_r.count(max_i) < list_r.count(i):
            max_i = list_r.index(i)
    print(list_r)
    print(f'Число {list_r[max_i]} выпало {list_r.count(max_i)} раз(а)')        
    
if __name__ == '__main__':
    frequent_number()
