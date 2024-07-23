from main import longest_substring
import pytest

def test_01():
    assert 3 == longest_substring('abcabcbb')

def test_02():
    assert 1 == longest_substring('bbbbb')

def test_03():
    assert 3 == longest_substring('pwwkew')