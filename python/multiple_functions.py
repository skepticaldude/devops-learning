# Functions can return multiple values using tuples:

def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 3, 9, 2])
print(f"Minimum: {minimum}, Maximum: {maximum}")

# this function returns the minimum and maximum from the set of numbers you give i (we can call that a tuple ). then i'm still yet to understand wether the numbers in the argument is a defualt thing or not,
