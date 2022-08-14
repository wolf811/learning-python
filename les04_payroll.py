# Расчет заработной платы
def payroll():
    try:
        output = float(input("Выработка в часах: "))
        rate = float(input("Ставка в час: "))
        prize = float(input("Премия: "))
        res = ((output * rate) + prize)
        return f'{res} руб.'

    except TypeError:
        print("Неверные входные данные! Укажите ввод в числовом формате.")
    except ValueError:
        print("Неверные входные данные! Укажите ввод в числовом формате.")


