def factorial_gen(n):
    start = 1
    fact = 1
    for start in range(n):
        yield fact
        start += 1
        fact *= start
    print(fact)


fs = factorial_gen(4)
for i in fs:
    print(i)
