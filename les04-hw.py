from les04_payroll import payroll
from functools import reduce
# ============= Задание 1 ===========
# print(payroll())

# ============= Задание 2 ===========
# first_list = [2, 52, 86, 123, 100]
# second_list = [el+1 for el in first_list]
# print(f"Первый список: {first_list}")
# print(f"Второй список: {second_list}")

# ============= Задание 3 ===========
# print([el/20 or el/21 for el in range(20, 240)])

# ============= Задание 4 ===========
# list_a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# list_b = [i for i in list_a if list_a.count(i) == 1]
# # list_b = []
# # for i in list_a:
# #     if list_a.count(i) == 1:
# #         list_b.append(i)
# print(list_b)

# ============= Задание 5 ===========
# start, stop, step = 100, 1000, 2
# stop += step 
# list_c = [i for i in range(start, stop, step)]
# # def reduce_list(x,y):
# #     return x * y
# # print(reduce(reduce_list, list_c))
# reduce_list = reduce(lambda x,y: x * y, list_c)
# print(reduce_list)

# ============= Задание 6 ===========


# ============= Задание 7 ===========
