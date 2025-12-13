#lambda function with mapping

numbers = [4,6,8,9,6,5,3]
square_numbers = list(map(lambda x: x ** 2, numbers))
print(square_numbers)