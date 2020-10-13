with open('text_6.txt', 'r', encoding='utf-8') as zadanie6_txt:
    content = zadanie6_txt.readlines()
    dict_items = {}
    for line in content:
        item_name = line.partition(' ')[0]
        sum_number = 0
        number = 0
        for element in line:
            try:
                element = int(element)
                if isinstance(element, int):
                    number *= 10
                    number += element
            except BaseException:
                sum_number += number
                number = 0
        dict_items.update({f'{item_name}': sum_number})
print(dict_items)
