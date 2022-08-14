# TASK_1
# with open("text.txt", 'w', encoding='utf-8') as text:
#     while True:
#         line = input('input text: ')
#         if line == "":
#             break
#         else:
#             text.write(f"{line}\n")
# ============
# with open("text.txt", 'r', encoding='utf-8') as my_f:
#     content = my_f.read()
#     print(content)

# TASK_2
# from math import sum
with open("text.txt", 'r', encoding='utf-8') as text:
    lines = text.read()
    print(lines)
    for line in lines:
        print(line.count("\n"))
    # line = text.readlines()
    # print(line.split(""))
    # print(line.count("\n"))
# TASK_3

# TASK_4

# TASK_5

# TASK_6

# TASK_7
