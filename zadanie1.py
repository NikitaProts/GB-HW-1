from sys import argv

# output - выроботка salary - зп rate - ставка prize- премия
script_name, output, rate, prize = argv


def salary(output, rate, prize):
    salary = (int(output) * int(rate)) + int(prize)
    print(salary)


salary(output, rate, prize)
