def person(name, last_name, year_of_birth, city, email, telephone_number):
    print(name, last_name, year_of_birth, city, email, telephone_number)


person(
    name=input('Введите своё имя: '),
    last_name=input('Введите свою фамилию: '),
    year_of_birth=int(input('Введите год рождения: ')),
    city=input('Введите город проживания: '),
    email=input('Введите свой email: '),
    telephone_number=int(input('Введите свой номер телефона: ')),
)
