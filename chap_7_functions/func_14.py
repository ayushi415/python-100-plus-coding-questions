# password strength checker

def is_strong_password(password):
    """
    Checks if the password is strong or not.
    """
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    special_characters = '!@#$%^&*()-_+=[]{}|;:,.<>?/\\'
    if not any(char in special_characters for char in password):
        return False
    return True

print(is_strong_password('AbAbaBaB'))  # Output: False
print(is_strong_password('Str0ngPwd!'))  # Output: True