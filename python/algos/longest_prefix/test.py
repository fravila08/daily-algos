from main import longestPrefix
import pytest


def test_01():
    assert longestPrefix(["flower", "flow", "flight"]) == "fl"

def test_02():
    assert longestPrefix(["dog", "racecar", "car"]) == ""