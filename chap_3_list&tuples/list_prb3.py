#accessing list elements

# print the first, middle and last elements of the list

fruits=["apple","guava","mango","pomegranate","cherry"]

first=fruits.pop(0)
print(f"First element :{first}")

last=fruits.pop()
print(f"Last elements :{last}")

middle=fruits.pop(len(fruits)//2)
print(f"Middle element :{middle}")




