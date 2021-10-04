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
        day_valid = day if day in range(1, 32) else print("Такой даты не бывает")
        month_valid = month if month in range(1, 13) else print("Такого месяца нет")
        year_valid = year if year in range(1900, 2025) else print("Год не находится в нужном диапазоне")

date_numb = Date.get_number(12,4,1985)

Date.get_valid(12, 4, 1985)
