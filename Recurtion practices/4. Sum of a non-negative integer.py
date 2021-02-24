def sumDigits(num, the_sum=0):
    if not num:
        return the_sum
    num = str(num)
    return int(num[0]) + sumDigits(num[1:])


print(sumDigits(345))
print(sumDigits(45))
