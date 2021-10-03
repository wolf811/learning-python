from random import randrange
# ============= Задание 1 ===========
class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mtr = [[randrange(0,10) for y in range(col)] for x in range(row)]
        for el in range(col):
            print(self.mtr[el])
        print("===============")

    def __str__(self):
        for self.row in self.mtr:
            return i
            

    def __add__(self):
        pass

matrix = Matrix(3,3)
# matrix_str = Matrix(3, 3)
print(matrix)


# ============= Задание 2 ===========

