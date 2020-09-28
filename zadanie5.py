proceeds = float(input('Enter proceeds'))  # Выручка
costs = float(input('Enter costs'))  # Издержки

if proceeds > costs:
    print('Выручка больше издержек')
    print(f'Соотношение выручка/издержки = {proceeds/costs}')
    profit = proceeds - costs  # Прибыль
    staff = int(input('Enter number of staff'))
    print(f'Каждый работяга получит по {profit/staff} единиц местной валюты')
elif proceeds < costs:
    print('Убыток')
