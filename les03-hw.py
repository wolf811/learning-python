# ============= Задание 1 ===========

# def division ():
#     while True:
#         try:
#             a = int(input("Введите первое число: "))
#             b = int(input("Введите второе число: "))
#             return (a / b)
#             break
#         except ZeroDivisionError:
#             print('На ноль делить нельзя! Повторите')

# print(division())

# ============= Задание 2 ===========

# def user (**kwargs):
#     res = list(kwargs.values())
#     return ', '.join(res)

# print(user(name = 'Валентин', surname = 'Комбаров', year = '1981', city = 'Домодедово', email = 'wolf811@gmail.com', phone = '89773570448' ))

# ============= Задание 3 ===========

def my_func(a,b,c):
    my_list = [a,b,c]
    n_min = my_list.remove(min(my_list))
    return sum(my_list)
print(my_func(10,5,6))

# ============= Задание 4 ===========
# ============= Задание 5 ===========
# ============= Задание 6 ===========
