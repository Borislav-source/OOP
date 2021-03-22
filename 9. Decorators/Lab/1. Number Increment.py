def number_increment(numbers):
    def incrementation(nums):
        return [num + 1 for num in nums]
    return incrementation(numbers)


print(number_increment([1, 2, 3]))
