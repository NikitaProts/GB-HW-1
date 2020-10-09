from random import randint
b = []
a = [randint(-100, 100) for i in range(randint(5, 10))]


for i in a:
    if a.index(i) == 0:
        continue
    if i > a[a.index(i) - 1]:
        b.append(i)

print(b)
