# Merging Dictionaries

# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares.
#  Merge these dictionaries into a single dictionary and print it.

d1 = {i: i**2 for i in range(1, 6)}
d2 = {i: i**2 for i in range(6, 11)}
d1.update(d2)
print(d1)