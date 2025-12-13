# Create a list and print all the even numbers from the list

lst = list(range(1, 21))
print(lst)

evens = [x for x in lst if x % 2 == 0]
print("Even numbers from the list are :\n",evens)