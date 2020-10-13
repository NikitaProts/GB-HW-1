with open('text_3.txt', 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    svg_salary = 0
    count_employees = 0
    for line in content:
        count_employees += 1
        employee_in_line = line.split()[0]
        for element in line.split():
            try:
                element = float(element)
                if isinstance(element, float):
                    svg_salary += element
                if element < 20000:
                    print(
                        f'{employee_in_line} имеет зп менее 20 000, а именно  = {element}')
            except BaseException:
                continue

    svg_salary /= count_employees
    print(
        f'Всего сотрудников = {count_employees}  и их средняя зарплата = {svg_salary}')
