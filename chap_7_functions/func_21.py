 # convert a list of strings to integers using mapping:

string_numbers = ['1', '2', '3']
int_numbers = list(map(int, string_numbers))
print(int_numbers)

#convert all words in a list to uppercase using mapping:

words = ['apple', 'banana', 'cherry']
upper_words = list(map(str.upper, words))
print(upper_words)

# applying mapping to list of dictonaries

def get_name(person):
    return person['name']
people = [
    {'name': 'Krush', 'age': 32},
    {'name': 'Jack', 'age': 33}
]
names = list(map(get_name, people))
print(names)


