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
with open(r"les05-hw_for_file/f_task3.txt", encoding="utf-8") as f_task3:
    
    lines = f_task3.readlines()
    average = sum
    for line in lines:
        lst_line = line.split()
        lst_line[1] = int(lst_line[1])
        # for i in range(len(lst_line)):
        #     try:
        #         lst_line[i] = int(lst_line[i])
        #     except ValueError:
        #         pass

        if lst_line[1] < 20000:
            print(f"Сотрудник с зарплатой менее 20 000 руб.: \n {line}")
        # average = lst_line[1] * 5 / 
        # print(average)


# ============= Задание 4 ===========
# ============= Задание 5 ===========

# ============= Задание 6 ===========
