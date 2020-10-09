from itertools import count, cycle

# Задание а)
start_number = int(input("Введите первое число"))
stop_number = int(input("Введите последнее число"))
for el in count(start_number):
    if el > stop_number:
        break
    else:
        print(el)

# Задание б)
user_cyrcle = input("Введите список").split()
user_count_stop = int(input("Введите кол-во повторов")) - \
    1  # тк счёт начинается с 0

с = 0
for el in cycle(user_cyrcle):
    if с > user_count_stop:
        break
    print(el)
    с += 1
