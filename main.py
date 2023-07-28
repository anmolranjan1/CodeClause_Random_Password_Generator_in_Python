import random
import string

def generate_password(length=12, use_digits=True, use_uppercase=True, use_lowercase=True, use_symbols=True):
    """
    Generate a random password with specified length and character sets.

    Parameters:
        length (int): The length of the password (default is 12).
        use_digits (bool): Whether to include digits in the password (default is True).
        use_uppercase (bool): Whether to include uppercase letters in the password (default is True).
        use_lowercase (bool): Whether to include lowercase letters in the password (default is True).
        use_symbols (bool): Whether to include symbols in the password (default is True).

    Returns:
        str: The randomly generated password.
    """

    # Define character sets
    digits = string.digits if use_digits else ''
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    lowercase_letters = string.ascii_lowercase if use_lowercase else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine character sets
    combined_characters = digits + uppercase_letters + lowercase_letters + symbols

    # Ensure at least one character from each set is included
    password = []
    if use_digits:
        password.append(random.choice(digits))
    if use_uppercase:
        password.append(random.choice(uppercase_letters))
    if use_lowercase:
        password.append(random.choice(lowercase_letters))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password with random characters
    remaining_length = max(length - len(password), 0)
    for _ in range(remaining_length):
        password.append(random.choice(combined_characters))

    # Shuffle the password to mix characters randomly
    random.shuffle(password)

    # Convert the list of characters to a string
    final_password = ''.join(password)

    return final_password

# Example usage:
if __name__ == "__main__":
    password1 = generate_password()
    print("Generated Password 1:", password1)

    password2 = generate_password(length=16, use_digits=False)
    print("Generated Password 2:", password2)
