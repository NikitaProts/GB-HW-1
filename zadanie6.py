tovar_list = []
user_exit = False
counter_tovar = 0
print('Выберите действие')
print('1 - Добавить запись\n2 - Вывести аналитику\n3 - Выход из программы \n')

while not user_exit:
    choice = int(input())
    # 1. Добавить запись
    if choice == 1:
        name = input('Введите название товара:')
        price = input('Введите цену товара: ')
        quantity = input('Введите кол-во товара: ')
        unit = input(
            'Введите еденицу измерения(например шт./кг и т.д.) товара: ')
        tovar = {
            'название': name,
            'цена': price,
            'количество': quantity,
            'ед': unit,
        }
        counter_tovar += 1
        tovar_tuple = (counter_tovar, tovar)
        tovar_list.append(tovar_tuple)
        print('Товар добавлен!')
        print('Выберите действие')
        print('1 - Добавить запись\n2 - Вывести аналитику\n3 - Выход из программы \n')

    # 2. Вывести аналитику
    if choice == 2:
        analytics_dict = {
            'название': [],
            'цена': [],
            'количество': [],
            'ед': [],
        }
        for tovar_in_list in tovar_list:
            for element in tovar_in_list:
                if isinstance(element, dict):
                    for key, value in element.items():
                        if key == 'название':
                            analytics_dict['название'] += [value]
                        if key == 'цена':
                            analytics_dict['цена'] += [value]
                        if key == 'количество':
                            analytics_dict['количество'] += [value]
                        if key == 'ед':
                            analytics_dict['ед'] += [value]
        print(analytics_dict)
        print('Выберите действие')
        print('1 - Добавить запись\n2 - Вывести аналитику\n3 - Выход из программы \n')

    # 3. Выход из программы
    if choice == 3:
        user_exit = True
