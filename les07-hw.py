from random import randrange
from abc import ABC, abstractmethod
# ============= Задание 1 ===========
# class Matrix:
#     # def __init__(self, row, col):
#     #     self.row = row
#     #     self.col = col
#     #     self.mtr = [[randrange(0,10) for y in range(col)] for x in range(row)]
#     #     for el in range(self.col):
#     #         print(self.mtr[el])
#     #     print("===============")
#     def __init__(self, mtr):
#         self.mtr = mtr
#         print(self.mtr)

#     def __str__(self):
#         return '\n'.join(' '.join(map(str, row)) for row in self.mtr)

#     def __add__(self, other):
#         res = []
#         for i in range(len(self.mtr)):
#             row = []
#             for j in range(len(self.mtr[i])):
#                 row.append(self.mtr[i][j] + other.mtr[i][j])
#             res.append(row)
#         return Matrix(res)


# mtr = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("===============")
# print(mtr)
# print("===============")
# mtr2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# print(mtr + mtr2)
# print("===============")

# ============= Задание 2 ===========
# class Clothes(ABC):
#     def __init__(self, par):
#         self.par = par

#     @abstractmethod
#     def consumption(self):
#         pass

# class Coat(Clothes):
#     def __init__(self, par):
#         super().__init__(par)
#         print(f"Размер пальто {self.par}")

#     @property
#     def consumption(self):
#         return round(self.par / 6.5 + 0.5, 2)

# class Costume(Clothes):
#     def __init__(self, par):
#         super().__init__(par)
#         print(f'Рост костюма {self.par}')

#     @property
#     def consumption(self):
#         return round(self.par * 2 + 0.3, 2)

# coat = Coat(52)
# print(f"Расход ткани на пальто: {coat.consumption}")
# costume = Costume(1.73)
# print(f"Расход ткани на костюм: {costume.consumption}")
# print(f'Общий расход: {coat.consumption + costume.consumption}')

# ============= Задание 3 ===========
# class Cell:
#     def __init__(self, numb_cell):
#         self.numb_cell = int(numb_cell)
    
#     def __str__(self):
#         return f"Результат {self.numb_cell}"
        
#     def __add__(self, other):
#         return Cell(self.numb_cell + other.numb_cell)

#     def __sub__(self, other):
#         if self.numb_cell - other.numb_cell > 0:
#             return Cell(self.numb_cell - other.numb_cell)
#         return f'Ошибка'

#     def __mul__(self, other):
#         return Cell(self.numb_cell * other.numb_cell)

#     def __truediv__(self, other):
#         return Cell(self.numb_cell // other.numb_cell)

#     def make_order(self, el):
#         # Подсмотрел в разборе ДЗ
#         return (("*" * el) + "\n") * (self.numb_cell // el) + "*" * (self.numb_cell % el)

# cell_1 = Cell(12)
# cell_2 = Cell(15)
# sum_cell = cell_1 + cell_2
# sub_cell = cell_1 - cell_2
# mul_cell = cell_1 * cell_2
# truediv_cell = cell_1 / cell_2
# print(sum_cell)
# print(sub_cell)
# print(mul_cell)
# print(truediv_cell)
# print(cell_1.make_order(3))
# print("==========")
# print(cell_2.make_order(5))

