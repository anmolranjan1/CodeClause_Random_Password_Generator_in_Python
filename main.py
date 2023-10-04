import random
import string

def generate_password(length=None, use_digits=None, use_uppercase=None, use_lowercase=None, use_symbols=None):
    """
    Generate a random password with specified length and character sets.

    Parameters:
        length (int or None): The length of the password (default is None, which generates a password of length 12).
        use_digits (bool or None): Whether to include digits in the password (default is None, which includes digits).
        use_uppercase (bool or None): Whether to include uppercase letters in the password (default is None, which includes uppercase).
        use_lowercase (bool or None): Whether to include lowercase letters in the password (default is None, which includes lowercase).
        use_symbols (bool or None): Whether to include symbols in the password (default is None, which includes symbols).

    Returns:
        str: The randomly generated password.
    """

    # Default values if parameters are not provided
    length = length or 12
    use_digits = use_digits if use_digits is not None else True
    use_uppercase = use_uppercase if use_uppercase is not None else True
    use_lowercase = use_lowercase if use_lowercase is not None else True
    use_symbols = use_symbols if use_symbols is not None else True

    # Define character sets
    digits = string.digits if use_digits else ''
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    lowercase_letters = string.ascii_lowercase if use_lowercase else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine character sets
    combined_characters = digits + uppercase_letters + lowercase_letters + symbols

    # Ensure at least one character from each set is included
    password = [
        random.choice(digits) if use_digits else '',
        random.choice(uppercase_letters) if use_uppercase else '',
        random.choice(lowercase_letters) if use_lowercase else '',
        random.choice(symbols) if use_symbols else '',
    ]

    # Fill the rest of the password with random characters
    remaining_length = max(length - sum(map(len, password)), 0)
    password.append(''.join(random.choices(combined_characters, k=remaining_length)))

    # Shuffle the password to mix characters randomly
    password = ''.join(random.sample(''.join(password), len(''.join(password))))

    return password

# Example usage:
if __name__ == "__main__":
    password1 = generate_password()
    print("Generated Password 1:", password1)

    password2 = generate_password(length=16, use_digits=False)
    print("Generated Password 2:", password2)