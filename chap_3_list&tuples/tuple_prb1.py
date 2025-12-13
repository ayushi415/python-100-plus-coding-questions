# create a tuple with the first 10 positive numbers . 

tpl = tuple(range(1, 11))
print(tpl)

# Print the first, middle, and last elements of the tuple

print(f"First element: {tpl[0]}")
print(f"Middle element: {tpl[len(tpl) // 2]}")
print(f"Last element: {tpl[-1]}")

# Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple 

print(f"First three elements: {tpl[:3]}")
print(f"Last three elements: {tpl[-3:]}")
print(f"Elements from index 2 to 5: {tpl[2:6]}")