stroka = input('Введите строку')

for index, el in enumerate(stroka.split(), 1):
    if len(el) > 10:
        print(index, el[0:10])
    else:
        print(index, el)
