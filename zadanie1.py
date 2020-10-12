# Решение задания
with open('text_zadanie.txt', 'a') as f_obj:
    while True:
        user_str = input(
            "Введите ваше предложение и нажмите Enter, чтобы прекратить работу программы просто нажмите Enter")
        if user_str == '':
            print('Завершение программы!')
            break
        else:
            f_obj.write(user_str + '\n')

# Проверка
with open('text_zadanie.txt', 'r') as f_obj:
    content = f_obj.read()
    print(content)
