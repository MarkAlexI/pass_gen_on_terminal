import string
import pytest
from project import generate_password


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
