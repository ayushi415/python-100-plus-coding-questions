# Set Comprehensions
# Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.

squares = {x**2 for x in range(1, 11)}
print(squares)

# Frozenset
# Create a frozenset with the first 5 positive integers. Print the frozenset.

fs = frozenset(range(1, 6))
print(fs)