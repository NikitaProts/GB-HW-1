from googletrans import Translator
# https://pypi.org/project/googletrans/

translator = Translator()

with open('text_4.txt', 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    for line in content:
        translated = translator.translate(line, src='en', dest='ru')
        with open('zadanie4.txt', 'a', encoding='utf-8') as zadanie4_txt:
            zadanie4_txt.write(translated.text + '\n')
