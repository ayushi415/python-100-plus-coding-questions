#  Nested Dictionaries
#Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'.
#  Print the nested dictionary.

student = {
    'name': 'John Doe',
    'age': 16,
    'grades': {
        'math': 90,
        'science': 85,
        'english': 88
    }
}
print(student)