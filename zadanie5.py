def my_f():
    """Подсчет чисел в строке до появления q"""
    sum_user_str = 0
    user_exit = False
    while not user_exit:
        user_str = input(
            'Введите числа через пробел или для оставноки программы введите q: ')
        user_str = user_str.split()
        sum_timeline = 0
        for el in user_str:
            if el.isdigit():
                sum_user_str += int(el)
                sum_timeline += int(el)
            elif el == 'q':
                user_exit = True
                break
            else:
                print(
                    'Вы ввели не спец симфол и не число. Все числа в данной строке были посчитаны!')

        print(
            f'Сумма в данной строке = {sum_timeline}\nСумма всех строк = {sum_user_str} ')
        sum_timeline = 0


# Для проверки
# my_f()
