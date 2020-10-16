class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f"{self._income['wage'] + self._income['bonus']}")


a = Position('Иван', 'Иванов', 'Программист', 12, 21)
a.get_full_name()
a.get_total_income()
