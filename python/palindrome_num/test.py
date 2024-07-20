from main import palindrome
import pytest

def test_01():
    assert palindrome(121)

def test_02():
    assert not palindrome(-121)

def test_03():
    assert not palindrome(10)