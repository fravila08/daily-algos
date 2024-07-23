from main import zigzag_convert
import pytest

def test_01():
    assert 'PAHNAPLSIIGYIR' == zigzag_convert('PAYPALISHIRING', 3)

def test_02():
    assert 'PINALSIGYAHRPI' == zigzag_convert('PAYPALISHIRING', 4)

def test_03():
    assert 'A' == zigzag_convert('A', 1)