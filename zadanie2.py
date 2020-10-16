class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def coating(self):
        print(
            f'Необходимая масса  = {(self._length*self._width*25*5)/1000} т.')


a = Road(20, 5000)
a.coating()
