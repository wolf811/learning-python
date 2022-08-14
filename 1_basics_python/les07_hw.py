# TASK_1

# TASK_2
class Dress:
    def fabric_consumption(self):
        return f'Расход ткани'
class Coat(Dress):
    def __init__(self, v):
        self.v = v
    def fabric_consumption(self):
        return f''
class Suit(Dress):
    def __init__(self, h):
        self.h = h

# TASK_3
