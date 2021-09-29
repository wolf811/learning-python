# ============= Задание 1 ===========
class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self, time_green, time_red=7, time_yellow=2):
        print("Светофор запустили:")
        for i in TrafficLight.__color:
            if i == TrafficLight.__color[0]:
                print(f"{i} - {time_red} sec")
            elif i == TrafficLight.__color[1]:
                print(f"{i} - {time_yellow} sec")
            else:
                print(f"{i} - {time_green} sec")

run = TrafficLight()
run.running(8)

# ============= Задание 2 ============
class Road:
    _lenght = 0
    _width = 0

    def mass_asphalt(self, mass, depth):
        pass
