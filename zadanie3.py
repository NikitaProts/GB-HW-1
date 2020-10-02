dict_months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}
dict_season_in_year = {
    'зима': [dict_months[12], dict_months[1], dict_months[2]],
    'весна': [dict_months[3], dict_months[4], dict_months[5]],
    'лето': [dict_months[6], dict_months[7], dict_months[8]],
    'осень': [dict_months[9], dict_months[10], dict_months[11]]
}

number = int(input('Введите номер месяца: '))

for key, value in dict_months.items():
    if key == number:
        for season, months in dict_season_in_year.items():
            if value in months:
                print(season)
