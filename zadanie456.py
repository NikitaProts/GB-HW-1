class Stock:
    """Класс Склад"""

    def __init__(self, name):
        self.name = name
        self.list_tovar = []

    def __repr__(self):
        pass

    # добавление оргтехники
    def add_offeciquipment(self, offeciquipment):
        if isinstance(
                offeciquipment,
                Printer) or isinstance(
                offeciquipment,
                Scaner) or isinstance(
                offeciquipment,
                Xerox):
            print('Добавлен!')
            self.list_tovar.append(offeciquipment)
        else:
            print('Ошибка добавления!')

    # удаление оргтехники
    def delete_offeciquipment(self, offeciquipment):
        if isinstance(
                offeciquipment,
                Printer) or isinstance(
                offeciquipment,
                Scaner) or isinstance(
                offeciquipment,
                Xerox):
            print('Удаление!')
            self.list_tovar.remove(offeciquipment)
        else:
            print('Ошибка удаления!')

    # Передача оргтехники
    @staticmethod
    def transfer_offeciquipment(class_1, class_2, offeciquipment):
        if offeciquipment in class_1.list_tovar:
            class_1.delete_offeciquipment(offeciquipment)
            class_2.add_offeciquipment(offeciquipment)
            print('Перемещение завершено!')
        else:
            print('Оргтехники нет на складе!')


class OfficeEquipment:
    """Класс оргтехника"""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.list_office = [self.name, self.price, self.quantity]

    def __repr__(self):
        return str(self.list_office)


class Printer(OfficeEquipment):
    pass


class Scaner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


# создание складов
stock_1 = Stock('First')
stock_2 = Stock('Second')

# создание техники
printer = Printer('printer', 25, 23)
scaner = Scaner('scaner', 123, 321)

# добавление техники на склады
stock_1.add_offeciquipment(printer)
stock_2.add_offeciquipment(scaner)
print(stock_1.list_tovar)
print(stock_2.list_tovar)

# перевозка принтера из склада1 в склад2
Stock.transfer_offeciquipment(stock_1, stock_2, printer)
print(stock_1.list_tovar)
print(stock_2.list_tovar)

# удаление сканера из склада2
stock_2.delete_offeciquipment(scaner)
print(stock_2.list_tovar)
