from abc import ABC, abstractmethod


class Clothes(ABC):

    """Класс одежда"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    """Класс пальто"""

    def __init__(self, name, v):
        super().__init__(name)
        self.v = v
        print(f'перегрузка метода инит в изделии  {self.name}')

    @property
    def consumption(self):
        """абстрактный метод"""

        return (self.v / 6.5 + 0.5)


class Suit(Clothes):

    """Класс костюм"""

    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def consumption(self):
        """абстрактный метод"""

        return (self.h * 2 + 0.3)


# Проверка
coat = Coat('пальто', 6.5)
print(coat.consumption)

suit = Suit('костюм', 1)
print(suit.consumption)

print(f'Общий расход ткани = {suit.consumption + coat.consumption }')
