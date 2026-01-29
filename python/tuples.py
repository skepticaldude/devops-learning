coordinates = (3, 4)
print(coordinates)

print(coordinates[0])

print(coordinates[1])

# coordinates[0] = 5  # This will raise an error


person = ("Alice", 25, "Engineer")
name, age, occupation = person  # Tuple unpacking
print(f"{name} is {age} years old and works as an {occupation}.")

single_item_tuple = (42,)
print(type(single_item_tuple))


def get_dimensions():
    return (1920, 1080)

width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")
