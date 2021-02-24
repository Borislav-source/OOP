def list_sum(lst, the_sum=0, n=0):

    for el in lst:
        if not isinstance(el, list):
            the_sum += el
        else:
            the_sum = list_sum(el, the_sum)
    return the_sum


my_list = [1, 2, [3, 4], [5, 6]]
print(list_sum(my_list))
