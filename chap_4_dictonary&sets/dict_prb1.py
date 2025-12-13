#Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.

d = {i: i**2 for i in range(1, 11)}
print(d)

# Dictionary Methods
# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.

d[11] = 121
d.pop(1)
print(d)

# Iterating Over Dictionaries
# Iterate over the dictionary created in Assignment 1 and print each key-value pair.

for key, value in d.items():
    print(f"{key}: {value}")
