# ============= Задание 1 ===========
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        print(f"{day}-{month}-{year}")

    @classmethod
    def get_number(cls, day, month, year):
        try:
            return cls(int(day), int(month), int(year))
        except TypeError:
            print("Неверный тип данных")
        except ValueError:
            print("Неверный тип данных")

    @staticmethod
    def get_valid(day, month, year):
        if day in range(1, 32):
            return day
        elif month in range(1, 13):
            return month
        elif year in range(1900, 2025):
            return year
        else:
            print("Дата введена не правильно")
date_cls = Date("ddfd", 4, 1985)
# date_numb = Date.get_number(12, 4, 1985)
# print(date_cls.get_valid(12, 4, 1985))
