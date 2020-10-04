def isEnglish(s):
    """https://stackoverflow.com/questions/27084617/detect-strings-with-non-english-characters-in-python"""
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def int_func(text):
    user_str = ''
    for word in text.split():
        if isEnglish(word):
            for letter in word:
                if letter.isalpha() and letter.islower():
                    user_str += word.title() + ' '
                    break
                else:
                    pass
        else:
            print('Вы ввели сиволы не английского алфавита, а я работаю только с ними!')
    print(user_str)

# Для проверки
# int_func('hello привет world     1 2 краказябры!   ')
