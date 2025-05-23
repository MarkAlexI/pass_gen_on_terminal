import string
import random


def generate_password(length=12, use_digits=True, use_special_chars=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("No characters available for password generation.")

    return ''.join(random.choice(characters) for _ in range(length))


def is_strong_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return all([has_upper, has_lower, has_digit, has_special, len(password) >= 8])


def main():
    new_password = generate_password()
    print(new_password)

    if is_strong_password(new_password):
        print("This password is strong.")
    else:
        print("Warning: the password is not very secure.")


if __name__ == "__main__":
    main()
