class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def __gt__(self, other):
        return self.cell > other.cell

    def __str__(self):
        self.cell = str(self.cell)
        return self.cell

    def make_order(self, rows):
        while self.cell != 0:
            if rows <= self.cell:
                print('*' * rows + '\n')
                self.cell -= rows
            elif rows > self.cell:
                print('*' * (rows - (rows - self.cell)) + '\n')
                self.cell = 0


cell_1 = Cell(90)
cell_2 = Cell(89)

print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(f"{cell_1 - cell_2 if cell_1 > cell_2 else 'Eror!'}")  # cell_1 - cell_2
print(f"{cell_1 // cell_2 if cell_1 > cell_2 else 'Eror!'}")  # cell_1 - cell_2


cell_1.make_order(9)
print('_____________________________')
cell_2.make_order(11)
