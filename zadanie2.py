a = []
qwe = True

print('Для заполнения списка введите число. Для остановки заполнения списка нажмите Enter:')
while qwe:
    element = input()
    if element == '':
        qwe = False
    else:
        a.append(int(element))

print(a)
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
