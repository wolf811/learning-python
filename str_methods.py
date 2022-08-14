# TASK_1
# lst = [55, '123', 'Valentin', True, (1,2,3), ['a', 'b', 1]]
# print([f'{i} - {type(i)}' for i in lst])

# for i in lst:
#     print(f'{i} - {type(i)}')

# TASK_2
# lst = input('Введите значения через пробел: ').split()
# print(lst)
# lst[:-1:2], lst[1::2] = lst[1::2], lst[:-1:2]
# print(lst)

# TASK_3
# V-1
# lst = [i for i in range(1, 13)]
# print(lst)
# user = int(input('Введите число от 1 до 12: '))
# if user in range(3, 6):
#     print('Весна')
# elif user in range(6, 9):
#     print('Лето')
# elif user in range(9, 12):
#     print('Осень')
# elif user == 1 or user == 2 or user == 12:
#     print('Зима')
# else:
#     print('Введите число от 1 до 12!!!')

# V-2
# user = int(input('Введите число от 1 до 12: '))
# dct = {
#     "Зима": (1, 2, 12), 
#     "Весна": (3, 4, 5),
#     "Лето": (6, 7, 8),
#     "Осень": (9, 10, 11)
# }

# for k in dct.keys():
#     if user in dct[k]:
#         print(k)

# TASK_4
# str = input("Ввести строку через пробелы: ")
# lst = str.split()
# for i, el in enumerate(lst, 1):
#         print(i, el[:10])

# TASK_5
# lst = [7, 5, 3, 3, 2]
# user = int(input("Число от 0 до 9: "))
# lst.append(user)
# lst.sort()
# lst.reverse()
# print(lst)

# TASK_6
# products = []
# prod_el = {}

# while True:
#     prod_key = input('Характеристика товара: ')
#     prod_val = input('Значение характеристики: ')
#     if prod_key == "stop":
#         prod_el.update({prod_key: prod_val})
#         break
#     elif prod_key == 'next':
#         products.append(prod_el)
#         continue
    
# for i in enumerate(products, 1):
#     print(i)

