# ============= Задание 1 ===========

def division (*args):
    while True:
        try:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            return a / b
            break
        except ZeroDivisionError:
            print('На ноль делить нельзя! Повторите')

print(division())

# ============= Задание 2 ===========
# ============= Задание 3 ===========
# ============= Задание 4 ===========
# ============= Задание 5 ===========
# ============= Задание 6 ===========
