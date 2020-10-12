# Решение задания 1
with open('text_zadanie.txt', 'a') as f_obj:
    while True:
        user_str = input(
            "Введите ваше предложение и нажмите Enter, чтобы прекратить работу программы просто нажмите Enter ")
        if user_str == '':
            print('Завершение программы!')
            break
        else:
            f_obj.write(user_str + '\n')

# Задание 2
with open('text_zadanie.txt', 'r') as f_obj:
    count_str = 0
    content = f_obj.readlines()
    for letters in content:
        count_str +=1
        count_word = 0
        for element in letters.split():
            count_word +=1
        print(f'В строке "{letters}"  {count_word} слов')
    print(f'Всего строк в файле {count_str}')

