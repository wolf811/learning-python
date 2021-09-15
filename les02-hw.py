# print("============ Задание 1 ==============".upper())

# first_list = [1, 2, 'abc', 3.14, ['a', 'b', 'c'], (1, 2, 3)]
# for i in first_list:
#     print(type(i))

# print("=====================================")

# print("============ Задание 2 ==============".upper())

# Наикривейший способ
# mylist = []
# i = 0
# n = 0
# while i < 5:
#     i += 1
#     n += 1
#     myval = input(f"Введите 5 любых значений, {n}-е: ")
#     mylist.append(myval)
# print(mylist)
# # if len(mylist) > 4 and len(mylist) % 2 != 0:
# f_el = mylist.pop(0)
# mylist.insert(1, f_el)
# n_el = mylist.pop(2)
# mylist.insert(3, n_el)
# print(mylist)

# print("=====================================")

# print("============ Задание 3 ==============".upper())
# # !!!! НАПИСАТЬ ЕЩЕ ЧЕРЕЗ СПИСОК, а лучше сразу переделать
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
mydict = {
    'Зима': [12, 1, 2],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11]
}
w = mydict.get('Зима')
print(w)
# print("=====================================")

# print("============ Задание 4 ==============".upper())

# text = (input("Введите строку из нескольких слов: ").split())
# for ind, el in enumerate(text, 1):
#     print(ind, el[:10])

# print("=====================================")

# print("============ Задание 5 ==============".upper())

# mylist2 = [7, 5, 3, 3, 2]

# el = int(input("Новый элемент рейтинга: "))
# mylist2.append(el)
# mylist2.sort()
# mylist2.reverse()
# # print(sorted(mylist2, reverse=True))
# print(mylist2)

# print("=====================================")

# print("============ Задание 6 ==============".upper())



# print("=====================================")
