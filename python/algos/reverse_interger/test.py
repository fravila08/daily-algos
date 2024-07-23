from main import reverse_interger
import pytest

def test_01():
    assert 321 == reverse_interger(123)

def test_02():
    assert -321 == reverse_interger(-123)

def test_03():
    assert 21 == reverse_interger(120)