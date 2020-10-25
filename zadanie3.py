class UserErrorList:
    def __init__(self, *args):
        self.user_list = []

    def user_input(self):
        while True:
            try:
                number = int(input('Введите число или stop = '))
                self.user_list.append(number)
            except BaseException:
                user_exit = input('Для выхода напишите stop')
                if user_exit == 'stop':
                    print(self.user_list)
                    break
                else:
                    print('Только число!')


try_user_list = UserErrorList(1)
print(try_user_list.user_input())
