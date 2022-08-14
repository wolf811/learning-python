# TASK_1
# def zap(a,b,s):
#     try:
#         return int(a) * int(b) + int(s)
#     except ValueError:
#         print('Введите числа!')

# print(zap(input('Выработка в часах: '), input('Ставка: '), input('Премия: ')))

from sys import argv

# def zap(a, b, s):
#     return a * b + s

# try:
#     script, n1, n2, n3 = argv
# except ValueError:
#     n1 = input('Выработка в часах: ')
#     n2 = input('Ставка: ')
#     n3 = input('Премия: ')

# print(zap(int(n1), int(n2), int(n3)))

# TASK_2 ???????????????
# lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# lst_new = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i-1]]
# # for i in range(1, len(lst)):
# #     if lst[i] > lst[i-1]: 
# #         lst_new.append(lst[i])

# print(lst_new)

# TASK_3
# print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

# TASK_4
# lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# # lst_new = []
# # for i in lst:
# #     cnt = lst.count(i)
# #     print(f'{i} - {cnt}')
# #     if cnt == 1:
# #         lst_new.append(i)
# lst_new = [i for i in lst if lst.count(i) == 1]
# print(lst)
# print(lst_new)

# TASK_5
from functools import reduce
# V1
def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, [el for el in range(2, 12, 2)]))

# V2
lst = [el for el in range(2, 12, 2)]
my_func = lambda prev_el, el: prev_el * el
print(reduce(my_func, lst))

# TASK_6
# from itertools import count, cycle

# for el in count(3):
#     if el > 10:
#         break
#     else:
#         print(el)

# lst = ['Папа', 'молодец']
# i = 0
# for el in cycle(lst):
#     if i > 10:
#         break
#     else:
#         print(el)
#         i += 1

# TASK_7 ?????????????
# def gen():
#     for el in fact(n):
#         yield 

# def generator():
#     for el in (10, 20, 30):
#         yield el

# g = generator()
# print(g)

# for el in g:
#     print(el)