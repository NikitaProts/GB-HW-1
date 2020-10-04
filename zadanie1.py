def my_f(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return 'Деление на ноль!'


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
print(my_f(number_1, number_2))
