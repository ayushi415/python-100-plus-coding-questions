# Palindrome Checker

def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

print(is_palindrome('A man a plan a canal Panama'))  # Output: True
print(is_palindrome('hello'))  # Output: False