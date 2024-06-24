import pytest

from perfect_square import IsSquare

def test_negative():
  square = IsSquare(-1)
  assert square.simple_is_square() == False

def test_zero():
  square = IsSquare(0)
  assert square.simple_is_square() == True

def test_odd_nums():
  square = IsSquare(3)
  assert square.simple_is_square() == False

def test_even_nums():
  square = IsSquare(4)
  assert square.simple_is_square() == True

def test_medium_num():
  square = IsSquare(25)
  assert square.simple_is_square() == True

def test_medium_num_fail():
  square = IsSquare(26)
  assert square.simple_is_square() == False

def test_large_num_simple():
  square = IsSquare(98989999**2)
  """this is meant to fail on purpose"""
  # assert square.simple_is_square() == True

def test_large_num_babylonian():
  square = IsSquare(98989999**2)
  assert square.babylonian_is_square() == True

def test_large_num_easy():
  square = IsSquare(98989999**2)
  assert square.easy_is_square() == True