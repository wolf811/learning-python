from random import randrange
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
# class Clothes:
#     pass


# ============= Задание 3 ===========
# class Cell:
#     def __init__(self, numb_cell):
#         self.numb_cell = int(numb_cell)
        
#     def __add__(self, other):
#         return Cell(self.numb_cell + other.numb_cell)
        

#     def __sub__(self):
#         pass

#     def __mul__(self):
#         pass

#     def __truediv__(self):
#         pass

#     def make_order(self):
#         pass

# cell_1 = Cell(3)
# cell_2 = Cell(2)
# sum_cell = cell_1 + cell_2
# print(sum_cell)

import re
s = "sfsfd"
f = re.findall(r'sfdsd',s)
print(f)
