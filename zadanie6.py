with open('text_6.txt', 'r', encoding='utf-8') as zadanie6_txt:
    content = zadanie6_txt.readlines()
    dict_items = {}
    for line in content:
        for element in line.split('('):
            print(element)
            try:
                element = float(element)
                if isinstance(element, float):
                    print(element)
            except BaseException:
                continue