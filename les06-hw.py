# ============= Задание 1 ===========
# class TrafficLight:
#     __color = ["Red", "Yellow", "Green"]

#     def running(self, time_green, time_red=7, time_yellow=2):
#         print("Светофор запустили:")
#         for i in TrafficLight.__color:
#             if i == TrafficLight.__color[0]:
#                 print(f"{i} - {time_red} sec")
#             elif i == TrafficLight.__color[1]:
#                 print(f"{i} - {time_yellow} sec")
#             else:
#                 print(f"{i} - {time_green} sec")

# run = TrafficLight()
# run.running(5)

# ============= Задание 2 ============
# class Road:
#     _lenght = 15000
#     _width = 25

#     def mass_asphalt(self, mass, depth):
#         res = int(Road._lenght * Road._width * mass * depth / 1000)
#         print(f"Необходимая масса асфальта составляет: {res} тонн.")

# x = Road()
# x.mass_asphalt(35, 10)

# ============= Задание 3 ============
# class Worker:
#     name = "Евгений"
#     surname = "Иванов"
#     position = "инженер-программист"
#     _income = {}

# class Position(Worker):
#     def get_full_name(self):
#         print(f"Работник: {Worker.surname} {x.name}")

#     def get_total_income(self, wage, bonus):
#         Worker._income = {"wage": wage, "bonus": bonus}
#         total_income = sum(Worker._income.values())
#         print(f"{x.surname} {x.name} имеет доход {total_income} руб.")

# x = Worker()
# y = Position()
# print(f"Работник: {x.surname} {x.name}; должность: {x.position} ")
# y.get_full_name()
# y.get_total_income(100000, 50000)
# print(y.name, y.surname, y.position)

# ============= Задание 4 ============
class Car:
    pass