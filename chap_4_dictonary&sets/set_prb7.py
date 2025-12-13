#  Set Operations

# Create two sets: one with the first 5 positive integers and another with the first 5 even integers.
#  Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.

set1 = set(range(1, 6))
set2 = set(range(2, 11, 2))
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")
