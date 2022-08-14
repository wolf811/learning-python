# print("============ Задание 1 ==============".upper())

# first_list = [1, 2, 'abc', 3.14, ['a', 'b', 'c'], (1, 2, 3)]
# for i in first_list:
#     print(type(i))

# print("============ Задание 2 ==============".upper())

# Вариант найден в интернете, самому не получилось решить
# mylist = list(input("Введите любые символы: "))
# print(mylist)
# el = 0
# for i in range(int(len(mylist)/2)):
#     mylist[el], mylist[el + 1] = mylist[el + 1], mylist[el]
#     el += 2
# print(mylist)

# print("============ Задание 3 ==============".upper())

# # Вариант 1
# my_dict = {
#     1: 'зима',
#     2: 'зима',
#     3: 'весна',
#     4: 'весна',
#     5: 'весна',
#     6: 'лето',
#     7: 'лето',
#     8: 'лето',
#     9: 'осень',
#     10: 'осень',
#     11: 'осень',
#     12: 'зима',
# }
# while True:
#     try:
#         numb = int(input('Введите число от 1 до 12: '))
#         break
#     except ValueError:
#         print('Введите число!!!')

# res = my_dict.get(numb)
# print(res)

# Вариант 2
# n = int(input("Введите число от 1 до 12: "))
# mydict = {
#     'Зима': [12, 1, 2],
#     'Весна': [3, 4, 5],
#     'Лето': [6, 7, 8],
#     'Осень': [9, 10, 11]
# }
# a = mydict.get('Зима')
# b = mydict.get('Весна')
# c = mydict.get('Лето')
# d = mydict.get('Осень')
# if n in a:
#     print("Зима")
# elif n in b:
#     print("Весна")
# elif n in c:
#     print("Лето")
# else:
#     print("Осень")

# Вариант 3
# mydict = {
#     'Зима': [12, 1, 2],
#     'Весна': [3, 4, 5],
#     'Лето': [6, 7, 8],
#     'Осень': [9, 10, 11]
# }
# mylist3 = list(mydict.values())
# while True:
#     try:
#         n = int(input('Введите число от 1 до 12: '))
#         break
#     except ValueError:
#         print('Введите число!!!')

# if n in mylist3[0]:
#     print("Зима")
# elif n in mylist3[1]:
#     print("Весна")
# elif n in mylist3[2]:
#     print("Лето")
# else:
#     print("Осень")

# print("============ Задание 4 ==============".upper())

# text = (input("Введите строку из нескольких слов: ").split())
# for ind, el in enumerate(text, 1):
#     print(ind, el[:10])

# print("============ Задание 5 ==============".upper())

# mylist2 = [7, 5, 3, 3, 2]

# el = int(input("Новый элемент рейтинга: "))
# mylist2.append(el)
# mylist2.sort()
# mylist2.reverse()
# # print(sorted(mylist2, reverse=True))
# print(mylist2)

# print("============ Задание 6 ==============".upper())

# ЗАДАЧА НЕ РЕШЕНА!!!!!
# mytuple = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}), 
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]

# for i in mytuple:
#     mydict = i[1]
#     print(mydict)
#     k_mydict = mydict.keys()
#     print(k_mydict)

# count = 0
# while count < 3:
#     count += 1
#     number = int(input("Укажите порядковый номер товара: "))
#     for i in mydict:
#         p_name = input("Добавить товар: ")
#         mydict["название"] = p_name
#         print(mydict)
#     mylist.append((number, mydict))
#     mylist.sort()
#     print(mylist)
#     for i in mylist:
#         print(tuple(i))
# mytuple = mylist
# print(mytuple)
    # p_name = input("Добавить название: ")
    # p_price = float(input("Добавить цену: "))
    # p_sum = int(input("Добавить количество: "))
    # p_sum = input("Добавить еденицы измерения: ")

