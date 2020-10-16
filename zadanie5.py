class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Уникальное сообщение класса Pen')


class Pencil(Stationery):
    def draw(self):
        print('Уникальное сообщение класса Pencil')


class Handle(Stationery):
    def draw(self):
        print('Уникальное сообщение класса Handle')


stationery = Stationery('название')
stationery.draw()

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()
