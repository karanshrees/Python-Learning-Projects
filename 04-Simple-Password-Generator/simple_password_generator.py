import string
import random

def generate_password(length, include_lower=True, include_upper=True, include_numbers=True, include_symbols=True):
    pool = ''
    required_chars = []
    if include_lower:
        pool += string.ascii_lowercase
        required_chars.append(random.choice(string.ascii_lowercase))
    if include_upper:
        pool += string.ascii_uppercase
        required_chars.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        pool += string.digits
        required_chars.append(random.choice(string.digits))
    if include_symbols:
        pool += string.punctuation
        required_chars.append(random.choice(string.punctuation))

    if not pool:
        raise ValueError("Character pool is empty. Enable at least one character set.")

    if length < len(required_chars):
        raise ValueError(
            f"Password length {length} is too small for the {len(required_chars)} selected character types. "
            "Increase length or deselect some character types."
        )

    remaining = length - len(required_chars)
    rest = [random.choice(pool) for _ in range(remaining)]
    password_chars = required_chars + rest
    random.shuffle(password_chars)
    return ''.join(password_chars)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive integer for the password length.")
        else:
            include_lower = input("Include lowercase? (y/n): ").strip().lower().startswith('y')
            include_upper = input("Include uppercase? (y/n): ").strip().lower().startswith('y')
            include_numbers = input("Include numbers? (y/n): ").strip().lower().startswith('y')
            include_symbols = input("Include symbols? (y/n): ").strip().lower().startswith('y')

            password = generate_password(length, include_lower, include_upper, include_numbers, include_symbols)
            print(f"Generated Password: {password}")
    except ValueError as e:
        msg = str(e)
        if msg:
            print(msg)
        else:
            print("Invalid input. Please enter a valid integer for the password length.")
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled. Exiting.")
