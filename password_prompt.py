import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_symbols=True):
    try:
        validate_input(length, include_uppercase, include_digits, include_symbols)
    except ValueError as ve:
        print(f"Input validation error: {ve}")
        return None
    
    char_sets = [string.ascii_lowercase]
    if include_uppercase:
        char_sets.append(string.ascii_uppercase)
    if include_digits:
        char_sets.append(string.digits)
    if include_symbols:
        char_sets.append(string.punctuation)
    
    password = [random.choice(char_set) for char_set in char_sets]
    all_characters = ''.join(char_sets)
    password += [random.choice(all_characters) for _ in range(length - len(password))]
    
    random.shuffle(password)
    return ''.join(password)

def validate_input(length, include_uppercase, include_digits, include_symbols):
    if not isinstance(length, int) or length < 4:
        raise ValueError("Password length should be an integer and at least 4 characters.")
    if not (include_uppercase or include_digits or include_symbols):
        raise ValueError("At least one character type (uppercase, digits, symbols) must be included.")

def get_user_input():
    try:
        length = int(input("Enter password length (at least 4): "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        return length, include_uppercase, include_digits, include_symbols
    except ValueError:
        print("Invalid input. Please enter valid values.")
        return None, None, None, None

def main():
    while True:
        length, include_uppercase, include_digits, include_symbols = get_user_input()
        if length is not None:
            password = generate_password(length, include_uppercase, include_digits, include_symbols)
            if password:
                print("Generated Password:", password)
            break

if __name__ == "__main__":
    main()
