# list comprehensions

#create a list containing the squares of the first 10 positive integer using a list comprehension.print the new list

squares = [x**2 for x in range(1,11)]
print("The new list is :" ,squares)

# Filtring lists

#create a new list containing only the even numbers 
even_numbers = [x for x in range(1,11) if x % 2 == 0]
print("The list of even numbers is :",even_numbers)
