rating_list = []

qwe = True

print('Для заполнения списка введите число. Для остановки заполнения списка нажмите Enter:')
while qwe:
    element = input()
    if element == '':
        # Остановка заполнения
        qwe = False
    else:
        element = int(element)
        # Если элемент ЕСТЬ в списке рейтинга
        if element in rating_list:
            counter = 0
            for i in rating_list:
                if i == element:
                    counter += 1
                if counter == rating_list.count(element):
                    rating_list.insert(rating_list.index(i) + 1, element)
                    break
        # Если элемента НЕТ в списке рейтинга
        else:
            # Список пустой
            if len(rating_list) == 0:
                rating_list.append(element)
            else:
                if element >= max(rating_list):
                    rating_list.insert(0, element)
                if element <= min(rating_list):
                    rating_list.append(element)

print(rating_list)
