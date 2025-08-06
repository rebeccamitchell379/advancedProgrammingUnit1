import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(0, 5) == 5
    assert add(-3, 3) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)
