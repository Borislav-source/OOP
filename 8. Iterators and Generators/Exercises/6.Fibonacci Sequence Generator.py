def fibonacci(n=0):
    sequence = []
    n = 0
    while True:
        yield n
        sequence.append(n)
        if n == 0:
            n += 1
        else:
            n += sequence[-2]


generator = fibonacci()
for i in range(5):
    print(next(generator))
