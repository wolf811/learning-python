import math
# ============= Задание 1 ===========
# lst = []
# with open(r"les05-hw_for_file/f_task1.txt", 'w') as f_task1:
#     while True:
#         text = input("Введите текст: ")
#         lst.append(text + "\n")
#         if text == "":
#             break

#     f_task1.writelines(lst)
# print(lst)

# ============= Задание 2 ===========
# with open(r"les05-hw_for_file/f_task2.txt", encoding="utf-8") as f_task2:
#     lines = f_task2.readlines()
#     print("Количество строк в файле: ", len(lines))
#     i = 0
#     for line in lines:
#         i += 1
#         x = len(line.split())
#         print(f"Количество слов в строке {i}: {x}")

# ============= Задание 3 ===========
# with open(r"les05-hw_for_file/f_task3.txt", encoding="utf-8") as f_task3:
#     lines = f_task3.readlines()
#     mydict = {}
#     list_key = []
#     list_val = []
#     average = None
#     for line in lines:
#         lst_line = line.split()
#         lst_line[1] = int(lst_line[1])
#         # for i in range(len(lst_line)):
#         #     try:
#         #         lst_line[i] = int(lst_line[i])
#         #     except ValueError:
#         #         pass
#         # print(lst_line)
#         list_key.append(lst_line[0])
#         list_val.append(lst_line[1])
#         mydict.update(zip(list_key, list_val))
#     # print(list_key)
#     # print(list_val)
#     # print(mydict)
#     print("Сотрудники с окладом менее 20000:")
#     for x, y in mydict.items():
#         if y < 20000:
#             print(x, y)

#     average = sum(mydict.values()) / len(mydict)
#     print(f"Средняя величина дохода всех сотрудников состовляет: {average}")

# ============= Задание 4 ===========
# with open(r"les05-hw_for_file/f_task4.txt", encoding="utf-8") as f_task4:
#     lines = f_task4.readlines()
#     mydict= {}
#     list_key = []
#     list_val = []
#     list_ru = ['один', 'два', 'три', 'четыре']
#     for line in lines:
#         lst_line = line.split()
#         list_key.append(lst_line[0])
#         list_val.append(lst_line[2])
#         list_key = list_ru
#         mydict.update(zip(list_key, list_val))

#     for_file = [f"{x.title()} - {y}\n" for x, y in mydict.items()]
# with open(r"les05-hw_for_file/f_task4_w.txt", 'w', encoding="utf-8") as f_task4_w:
#     f_task4_w.writelines(for_file)

# ============= Задание 5 ===========
# with open(r"les05-hw_for_file/f_task5.txt", 'w', encoding="utf-8") as f_task5:
#     numb_input = input("Введите числа через пробел: ")
#     f_task5.write(numb_input)
# with open(r"les05-hw_for_file/f_task5.txt", 'r', encoding="utf-8") as f_task5:
#     line = f_task5.readlines()
#     for i in line:
#         lst = i.split()
#         for i in range(len(lst)):
#             try:
#                 lst[i] = int(lst[i])
#             except ValueError:
#                 pass
#     sum_lst = sum(lst)
#     print(f"Сумма чисел в файле равна: {sum_lst}")

# ============= Задание 6 ===========
with open(r"les05-hw_for_file/f_task6.txt", encoding="utf-8") as f_task6:
    lines = f_task6.readlines()
    mydict = {}
    list_key = []
    list_val = []
