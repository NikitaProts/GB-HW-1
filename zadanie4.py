from random import choice


class Car:
    def __init__(self, color, name, is_police=False):

        self.speed = choice([i for i in range(1, 101)])
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print(f"Машина повернула {choice(['налево', 'направо'])}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if (self.speed > 60):
            print(
                f'Машина {self.name} превышает скорость! Её скорость равна = {self.speed}')
        else:
            print(
                f'Машина {self.name} превышает не скорость. Её скорость равна = {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if (self.speed > 40):
            print(
                f'Машина {self.name} превышает скорость! Её скорость равна = {self.speed}')
        else:
            print(
                f'Машина {self.name} превышает не скорость. Её скорость равна = {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car = TownCar('black', 'town car')
town_car.go()
town_car.stop()
town_car.turn()
town_car.show_speed()

work_car = WorkCar('red', 'work_car')
work_car.go()
work_car.stop()
work_car.turn()
work_car.show_speed()

sport_car = SportCar('blue', 'sport_car')
sport_car.go()
sport_car.stop()
sport_car.turn()
print(f'ее скорость = {sport_car.show_speed()}')

police_car = PoliceCar('green', 'police_car', True)
police_car.go()
police_car.stop()
police_car.turn()
print(f'ее скорость = {police_car.show_speed()}')
