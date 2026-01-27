# Functions can return multiple values using tuples:

def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 3, 9, 2])
print(f"Minimum: {minimum}, Maximum: {maximum}")

# this function returns the minimum and maximum from the set of numbers you give i (we can call that a tuple ). then i'm still yet to understand wether the numbers in the argument is a defualt thing or not,

# this is from labex
###

# Python Multi-Value Returns

# Concept: Functions can return multiple results separated by commas.
# Mechanism: Python packs these values into a Tuple.
# Unpacking: You can assign the results directly to multiple variables in one line.
# Pro Tip: If you only need the maximum and want to ignore the minimum, developers often use an underscore for the unwanted value:
# _, maximum = min_max([1, 5, 3])


# Spoiler: Python will throw a ValueError because it expects the number of variables to match the number of returned items exactly!
###
