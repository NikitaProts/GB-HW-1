import time


class TrafficLight:

    def __init__(self):
        self.__colors = ['красный', 'желтый', 'зеленый']

    def running(self):
        while True:
            for color in self.__colors:
                if color == 'красный':
                    print(color)
                    time.sleep(7)
                    if 'зеленый' not in self.__colors:
                        self.__colors = self.__colors[::-1]
                        self.__colors.append('зеленый')
                        self.__colors.pop(0)
                elif color == 'желтый':
                    print(color)
                    time.sleep(2)

                elif color == 'зеленый':
                    print(color)
                    time.sleep(7)
                    self.__colors = self.__colors[::-1]
                    self.__colors.pop(0)
                    if 'красный' in self.__colors:
                        pass
                    else:
                        self.__colors.append('красный')


a = TrafficLight()
a.running()
