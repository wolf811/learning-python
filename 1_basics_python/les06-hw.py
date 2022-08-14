# TASK_1
from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for c in self.__color:
            if c == 'red':
                print(c)
                sleep(7)
            elif c == 'yellow':
                print(c)
                sleep(2)
            else:
                print(c)
                sleep(4)


run = TrafficLight()
# run.running()

# TASK_2


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.m1 = 25 / 1000
        self.b = 5

    def get_m(self):
        m_all = self._width * self._length * self.m1 * self.b
        print(f'Для дороги необходимо: {m_all} (т) асфальта')


a = Road(20, 5000)
# a.get_m()

# TASK_3


class Worker:
    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.pos = pos
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.surname} {self.name} ({self.pos}):'
        print(full_name)

    def get_total_income(self):
        print(sum(self._income.values()))


p = Position('Валентин', 'Kombarov', 'developer', 100000, 50000)
# p.get_full_name()
# p.get_total_income()

# TASK_4


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name}, {self.color} начала движение")

    def stop(self):
        print(f'Машина {self.name}, {self.color} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name}, {self.color} поехала {self.direction}')

    def show_speed(self):
        print(f'Ваша скорость - {self.speed} км/ч')

    def attention(self):
        if self.is_police == True and self.speed > 90:
            print(
                f'Автомобиль {self.name} {self.color} цвета прижмитесь к обочине!')


class TownCar(Car):
    def show_speed(self):
        print(f'Ваша скорость - {self.speed} км/ч')
        if self.speed > 60:
            print(f'Машина {self.name}, {self.color} превысила скорость')


class SportCar(Car):
    def go_police(self):
        if self.is_police == True and self.speed > 90:
            print('Ускоряемся!!!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Ваша скорость - {self.speed} км/ч')
        if self.speed > 40:
            print(f'Машина {self.name}, {self.color} превысила скорость')


class PoliceCar(Car):
    def attention(self):
        print('Остановись скотина!')


t_car = TownCar(65, 'белая', 'skoda', True)
s_car = SportCar(91, 'красная', 'ferrari', True)
w_car = WorkCar(70, 'синяя', 'gazel', True)
p_car = PoliceCar(120, 'черная', 'ГИБДД', True)

# t_car.go()
# t_car.show_speed()
# t_car.attention()
# t_car.turn('прямо')
# t_car.stop()
# print('======================')
# s_car.go()
# s_car.show_speed()
# s_car.attention()
# s_car.go_police()
# s_car.turn('налево')
# s_car.stop()
# print('======================')
# w_car.go()
# w_car.show_speed()
# w_car.attention()
# w_car.turn('направо')
# w_car.stop()
# print('======================')
# p_car.go()
# p_car.attention()

# TASK_5

class Stationery():
    def __init__(self,title):
        self.title = title
        
    def draw(self):
        print('Запуск отрисовки')
        
class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки - ручка')
class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки - карандаш')
class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки - маркер')
    
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

# pen.draw()
# pencil.draw()
# handle.draw()

