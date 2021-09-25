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
    my_dict = {}
    for i in lines:
        my_dict.update([i])
        print(my_dict)
# ============= Задание 4 ===========
# ============= Задание 5 ===========
# ============= Задание 6 ===========
