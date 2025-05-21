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


def main():
    new_password = generate_password()
    print(new_password)


if __name__ == "__main__":
    main()
