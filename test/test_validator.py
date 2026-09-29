# tests/test_validator.py
from validator import validate_email, validate_phone, validate_snils
def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False

def test_validate_phone():
    assert validate_phone("+79991234567") is True
    assert validate_phone("89991234567") is False
    assert validate_phone("+7999123") is False

def test_validate_snils():
    assert validate_snils("11223344595") == True
    assert validate_snils("001-001-999 32") == False
    assert validate_snils("123") == False
    assert validate_snils("123456789012") == False
    assert validate_snils("abcdefghijk") == False
    assert validate_snils("11223344500") == False
