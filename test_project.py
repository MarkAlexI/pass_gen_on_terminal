import string
import pytest
from project import generate_password
from project import is_strong_password


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
