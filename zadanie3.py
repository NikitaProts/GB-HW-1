number = int(input('Enter n: '))
number_1 = number * 10 + (number % 10)
number_2 = number_1*10 + (number % 10)
print(number, number_1, number_2)
print(number + number_1 + number_2)
