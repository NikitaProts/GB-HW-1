stroka = input('Введите строку')

for i in stroka.split():
    if len(i) > 10:
        print(i[0:10])
    else:
        print(i)
