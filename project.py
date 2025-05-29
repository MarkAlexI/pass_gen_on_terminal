import os
import string
import random
import argparse


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


def save_password_to_file(password, filename="passwords.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(password + "\n")


def load_passwords_from_file(filename="passwords.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
    parser.add_argument("-s", "--specials", action="store_true", help="Include special characters")
    parser.add_argument("-f", "--save", action="store_true", help="Save the generated password to file")
    parser.add_argument("-r", "--read", action="store_true", help="Display previously saved passwords")

    args = parser.parse_args()

    if args.read:
        print("Saved passwords:")
        passwords = load_passwords_from_file()
        for p in passwords:
            print("-", p)
    else:
        try:
            password = generate_password(args.length, args.digits, args.specials)
            print("Generated password:", password)
            if is_strong_password(password):
                print("This password is strong.")
            else:
                print("Warning: This password is not very strong.")
            if args.save:
                save_password_to_file(password)
                print("Password saved to file.")
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
