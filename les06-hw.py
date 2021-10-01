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
# class Car:

#     def __init__(self, name, color, speed, is_police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         print("========================")

#     def go(self):
#         print(f"Автомобиль {self.name} {self.color} цвета поехал")

#     def stop(self):
#         print(f"Автомобиль {self.name} {self.color} цвета остановился")

#     def turn(self, direction):
#         print(f"Автомобиль {self.name} {self.color} цвета движется {direction}, со скоростью {self.speed} км/ч ")

#     def show_speed(self):
#         print(f"Текущая скорость автомобиля {self.name} {self.color} цвета - {self.speed} км/ч")

# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             print("Вы превысили скорость, притормозите!")
#         else:
#             Car.show_speed(self)

# class SportCar(Car):
#     def show_speed(self):
#         if self.speed > 150:
#             print("Вы превысили скорость, притормозите!")
#         else:
#             Car.show_speed(self)

# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             print("Вы превысили скорость, притормозите!")
#         else:
#             Car.show_speed(self)

# class PoliceCar(Car):
#     def __init__(self, name, color, speed):
#         Car.__init__(self, name, color, speed, is_police=True)

# town_car = TownCar("Skoda", ",белого", 71)
# town_car.go()
# town_car.turn("прямо")
# town_car.show_speed()
# town_car.stop()

# sport_car = SportCar("Ferrari", "конечно красного", 185)
# sport_car.go()
# sport_car.turn("налево")
# sport_car.show_speed()
# sport_car.stop()

# work_car = WorkCar("Газель", "синего", 35)
# work_car.go()
# work_car.turn("направо")
# work_car.show_speed()
# work_car.stop()

# police_car = PoliceCar("Ford", "серого", 120)
# police_car.go()
# police_car.turn("налево")
# police_car.show_speed()
# police_car.stop()

# ============= Задание 5 ============
# class Stationery:
#     def __init__(self, title):
#         self.title = title

#     def draw(self):
#         print("Запуск отрисовки")

# class Pen(Stationery):
#     def draw(self):
#         print(f"Запуск отрисовки {self.title}")

# class Pencill(Stationery):
#     def draw(self):
#         print(f"Запуск отрисовки {self.title}")

# class Handle(Stationery):
#     def draw(self):
#         print(f"Запуск отрисовки {self.title}")

# pen = Pen("ручки")
# pencil = Pencill("карандаша")
# handle = Handle("маркера")
# pen.draw()
# pencil.draw()
# handle.draw()
