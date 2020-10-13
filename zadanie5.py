# запись
with open('zadanie5.txt', 'a', encoding='utf-8') as zadanie5_txt:
    numbers = input('Введите числа через пробел: ')
    zadanie5_txt.write(numbers + '\n')

# чтение
with open('zadanie5.txt', 'r', encoding='utf-8') as zadanie5_txt:
    content = zadanie5_txt.readlines()
    sum_in_file = 0
    for line in content:
        for element in line.split():
            try:
                element = float(element)
                if isinstance(element, float):
                    sum_in_file += element
            except BaseException:
                continue
    print(sum_in_file)
