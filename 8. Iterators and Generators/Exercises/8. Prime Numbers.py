from math import sqrt


def get_primes(lst):
    def check_if_number_is_prime(num):
        if num == 0 or num == 1:
            return False
        for n in range(2, int(sqrt(num))+1):
            if num % n == 0:
                return False
        return True
    for i in range(len(lst)):
        if check_if_number_is_prime(lst[i]):
            yield lst[i]


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))