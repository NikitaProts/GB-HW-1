class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_int(cls, list_date):
        list_date = list_date
        month = 0
        day = 0
        year = 0
        counter = 0
        for element in list_date.split('-'):
            counter += 1
            if counter == 1:
                day = int(element)
            elif counter == 2:
                month = int(element)
            elif counter == 3:
                year = int(element)
        return cls(day, month, year)

    @staticmethod
    def valid_date(self):
        # День 1-30 Месяц 1-12 Год 1-9999
        if (self.day >= 1 and self.day <= 30) and (self.month >=
                                                   1 and self.month <= 12) and (self.year >= 1 and self.year <= 9999):
            return 'Date is valid!'
        else:
            return 'date is not valid!'


# Date is not valid!
first_date = '21-1-19999'
my = Date.date_int(first_date)
print(my.valid_date(my))

# Date is  valid!
second_date = '21-1-1999'
my2 = Date.date_int(second_date)
print(my.valid_date(my2))
