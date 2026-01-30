fruits = {"apple", "banana", "cherry"}
print(fruits)

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

fruits.add("date")
print(fruits)

fruits.remove("banana")
print(fruits)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Union

print(set1.intersection(set2))  # Intersection

print(set1.difference(set2))  # Difference

print("apple" in fruits)

print("banana" in fruits)
