def my_func(var_1, var_2, var_3):
    """Сумма наибольших двух аргументов"""
    var_list = []
    var_list.extend([var_1, var_2, var_3])
    var_list.pop(var_list.index(min(var_list)))
    print(sum(var_list))

# Для проверки

# my_func(1,2,3)

# var_1 = int(input('Введите 1-й аргумент: '))
# var_2 = int(input('Введите 2-й аргумент: '))
# var_3 = int(input('Введите 3-й аргумент: '))
# my_func(var_1, var_2, var_3)
