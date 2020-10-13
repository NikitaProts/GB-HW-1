import json


with open('text_7.txt', 'r', encoding='utf-8') as zadanie7_txt:
    content = zadanie7_txt.readlines()
    company_list = []
    company_dict = {}
    avg_profit = 0
    count_company = 0
    for line in content:
        company_name = line.partition(' ')[0]
        profit = 0
        count_number = 0

        for element in line.split():
            try:
                element = float(element)
                if isinstance(element, float):
                    count_number += 1
                    if count_number < 2:
                        profit += element
                    else:
                        profit -= element
            except BaseException:
                continue
            if profit > 0 and count_number == 2:
                avg_profit += profit
                count_company += 1
        company_dict.update({f'{company_name}': profit})
    company_list.append(company_dict)
    avg_profit /= count_company
    average_profit_dict = {'average_profit': avg_profit}
    company_list.append(average_profit_dict)
    with open("zadanie7.json", "w", encoding='utf-8') as write_f:
        json.dump(company_list, write_f, ensure_ascii=False)
