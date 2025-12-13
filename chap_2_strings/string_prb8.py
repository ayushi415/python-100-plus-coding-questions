# check if a string is palindrome or not

word = input("Enter a word: ")

# reverse the string
reversed_word = word[::-1]

# check palindrome
if word == reversed_word:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
