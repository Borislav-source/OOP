def power(n, x):
    if x < 1:
        return 1
    return n * power(n, x-1)


print(power(3, 4))


