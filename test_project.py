import string
import pytest
from project import generate_password
from project import is_strong_password
from project import save_password_to_file
from project import load_passwords_from_file


# test generate_password
def test_default_length():
    password = generate_password()
    assert len(password) == 12


def test_custom_length():
    password = generate_password(length=20)
    assert len(password) == 20


def test_only_letters():
    password = generate_password(use_digits=False, use_special_chars=False)
    assert all(char in string.ascii_letters for char in password)
    assert any(char in string.ascii_letters for char in password)


def test_letters_and_digits():
    password = generate_password(use_special_chars=False)
    assert all(char in string.ascii_letters + string.digits for char in password)
    assert any(char in string.ascii_letters for char in password)
    assert any(char in string.digits for char in password)


def test_all_char_types():
    password = generate_password()
    assert all(char in string.ascii_letters + string.digits + string.punctuation for char in password)
    assert any(char in string.ascii_letters for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)


# test is_strong_password
def test_strong_password():
    assert is_strong_password("Abcdef1!")


def test_too_short():
    assert not is_strong_password("Ab1!")


def test_missing_uppercase():
    assert not is_strong_password("abcdef1!")


def test_missing_lowercase():
    assert not is_strong_password("ABCDEF1!")


def test_missing_digit():
    assert not is_strong_password("Abcdefg!")


def test_missing_special():
    assert not is_strong_password("Abcdefg1")


def test_only_special_and_digit():
    assert not is_strong_password("1234!@#$")


def test_exact_minimum_valid():
    assert is_strong_password("A1b2c3!@")


# test saving password to file
def test_save_password_to_file(tmp_path):
    # Arrange
    test_password = "Test123!"
    test_file = tmp_path / "test_passwords.txt"

    # Act
    save_password_to_file(test_password, filename=str(test_file))

    # Assert
    with open(test_file, "r", encoding="utf-8") as f:
        content = f.read().strip()
    assert content == test_password


def test_save_multiple_passwords_to_file(tmp_path):
    # Arrange
    passwords = ["Pass1!", "Secure123$", "MyPassword#2025"]
    test_file = tmp_path / "test_passwords.txt"

    # Act
    for pwd in passwords:
        save_password_to_file(pwd, filename=str(test_file))

    # Assert
    with open(test_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    assert lines == passwords


# test load_passwords_from_file
def test_load_passwords_from_existing_file(tmp_path):
    # Arrange
    passwords = ["abcDEF1!", "123qweRT$", "TestPass@2025"]
    test_file = tmp_path / "passwords.txt"
    for pwd in passwords:
        save_password_to_file(pwd, filename=str(test_file))

    # Act
    loaded_passwords = load_passwords_from_file(filename=str(test_file))

    # Assert
    assert loaded_passwords == passwords


def test_load_passwords_from_nonexistent_file(tmp_path):
    # Arrange
    non_existing_file = tmp_path / "no_such_file.txt"

    # Act
    passwords = load_passwords_from_file(filename=str(non_existing_file))

    # Assert
    assert passwords == []
