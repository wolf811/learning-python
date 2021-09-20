# ============= Задание 1 ===========

# def division (*args):
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

# def my_func(a,b,c):
#     my_list = [a,b,c]
#     n_min = my_list.remove(min(my_list))
#     return sum(my_list)
# print(my_func(10,5,6))

# ============= Задание 4 ===========
# x = int(input("Введите целое число: "))
# y = -int(input("Введите отрицательную степень: "))

# def myfunk(x,y):
#     res = x ** y
#     return res
# print(myfunk(x,y)

# НЕ РАБОТАЕТ!
# def myfunk2(x,y):
#     i = 1
#     res = 1
#     while i <= y:
#         res *= x
#         i += 1
#     return res
# print(myfunk2(x,y))

# ============= Задание 5 ===========

def sumnumber():
    text = input("Введите числа через пробел или 'end' для выхода: ")
    while text != "end":
        mylist = text.split()
        # intlist = [int(i) for i in mylist]
        for i in range(0, len(mylist)):
            mylist[i] = int(mylist[i])
        return sum(mylist)
    else:
        print('Вы вышли!')
print(sumnumber())

# def sumnumber():
#     global text 
#     text = input("Введите числа через пробел или 'end' для выхода: ")
#     mylist = text.split()
#     # intlist = [int(i) for i in mylist]
#     for i in range(0, len(mylist)):
#         mylist[i] = int(mylist[i])
#     return sum(mylist)

# print(sumnumber())

# while text != "end":
#     print(sumnumber())
# else:
#     print('Вы вышли!')
# ============= Задание 6 ===========
