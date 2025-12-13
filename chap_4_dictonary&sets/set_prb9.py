# Iterating Over Sets
#Create a set and iterate over the elements, printing each element.

s = set(range(1, 6))
for elem in s:
    print(elem)


# Removing Elements from Sets
#Create a set and remove elements from it until it is empty. Print the set after each removal.

s = set(range(1, 6))
while s:
    s.pop()
    print(s)