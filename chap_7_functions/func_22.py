# filters in functions

# checks whether a number is even and returns true or false,using filters.

def is_even(num):
    if num % 2 == 0:
        return True
    return False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

#using filter in lambda function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)