class ZeroDivisionClass(Exception):
    def __init__(self, txt):
        self.txt = txt


first_number = input("Числитель  = ")
second_number = input("Знаменитель = ")


try:
    first_number = int(first_number)
    second_number = int(second_number)
    if second_number == 0:
        raise ZeroDivisionClass("Знаменитель не может = 0")
except (ValueError, ZeroDivisionClass) as err:
    print(err)
else:
    print(first_number / second_number)
