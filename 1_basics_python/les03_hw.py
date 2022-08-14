# TASK_1
# def del_num(a, b):
#     try:
#         a, b = int(a), int(b)
#         print(a / b)
#     except ZeroDivisionError:
#         print('Деление на 0 запрещено')
#     except ValueError:
#         print('ValueError')
# del_num(input('Number a: '), input('Number b: '))

# TASK_2
# def user(firstname, lastname, year, city, email, phone):
#     lst = (f"Имя: {firstname}; Фамилия: {lastname}; год рождения: {year}; город: {city}; email: {email}; phone: {phone}").split('; ')
#     for i in lst:
#         print(i, '\n')

# user('Valentin', 'Kombarov', 1981, 'Kotovsk', 'wolf811@gmail.com', +79773570448)

# TASK_3
# def my_func(a,b,c):
#     lst = [a,b,c]
#     lst.remove(min(lst))
#     return sum(lst)
# print(my_func(1,1,0))

# TASK_4
# def my_func(x, y):
#     # var_1
#     return round(x**(-y), 3)
#     # var_2
#     # ?????
# print(my_func(1/2,1/2))

# TASK_5
# def sum_num():
#     res = 0

#     while True:
#         str_user = input('Enter numbers or "Q" for exit: ')
#         if str_user.upper() == 'Q':
#             break
#         str_user = str_user.split()
#         # for i in str_user:
#         #     if i.isdigit():

#         int_user = [int(i) for i in str_user]
#         res += sum(int_user)
#         print(res)

#     print(res)


# sum_num()

# TASK_6
# def int_func(str):
#     str.lower()
#     return str.title()
# def int_func(str): return str.title()


# print(int_func("HDFKHDKJ fslkjkl iosjfa IOROFkldjfsj"))
