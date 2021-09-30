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
    name = None
    color = None
    speed = None
    is_police = False

    # def __init__(self, name, color, speed):
    #     self.name = name
    #     self.color = color
    #     self.speed = speed
    #     self.is_police = False
    #     self.show_speed()

    def go(self):
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def direction(self):
        turn = {
            "go_left": "налево",
            "go_right": "направо",
            "go_straight": "прямо",
        }
        print(f"Автомобиль движется {turn}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} - {self.speed} км/ч")
        if town_car.speed > 60 or work_car.speed > 40:
            print("Вы превысили скорость")

class TownCar(Car):
    name = "Skoda"
    color = "серый"
    speed = 70

class SportCar(Car):
    name = "Ferrari"
    color = "красный"

class WorkCar(Car):
    name = "Gazel"
    color = "белый"
    speed = 50

class PoliceCar(Car):
    name = "Ford"
    color = "синий"
    is_police = True
    # print(f"Автомобиль {name}, {color}, максимальная скорость {max_speed} км/ч.")
    # if is_police:
    #     print("Предназначен для полиции.")

town_car = TownCar()
sport_car = SportCar()
work_car = WorkCar()
police_car = PoliceCar()

work_car.go()
work_car.show_speed()
work_car.direction()
work_car.stop()


