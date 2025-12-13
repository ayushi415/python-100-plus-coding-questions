# Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.

tpl = (1, 2, 2, 3, 4, 4, 4, 5)
print(f"Occurrences of 4: {tpl.count(4)}")
print(f"Index of first occurrence of 2: {tpl.index(2)}")


# tumple and list
# Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.

tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
lst.append(6)
tpl = tuple(lst)
print(tpl)