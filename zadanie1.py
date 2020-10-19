class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = [[0, 0], [0, 0], [0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        for i in result:
            for j in i:
                print(j, end=' ')
            print()
        return 'Сумма посчитана!'

    def __str__(self):
        for i in self.matrix:
            for j in i:
                print(j, end=' ')
            print()
        return ''


matrix_1 = Matrix([[1, 2], [2, 3], [3, 4]])
matrix_2 = Matrix([[9, 8], [7, 6], [5, 4]])

print(matrix_1)
print(matrix_2)

print(matrix_1 + matrix_2)
