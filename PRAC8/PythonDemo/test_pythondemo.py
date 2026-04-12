import pytest
import pythondemo

def test_add():
    assert pythondemo.add(2, 3) == 5

def test_multiply_fail():
    assert pythondemo.multiply(4, 3) == 11

def test_divide_by_zero():
    with pytest.raises(ValueError):
        pythondemo.divide(10, 0)

def test_is_even():
    assert pythondemo.is_even(4) is True
    assert pythondemo.is_even(5) is False

def test_factorial_basic():
    assert pythondemo.factorial(5) == 120
    assert pythondemo.factorial(0) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        pythondemo.factorial(-3)

def test_factorial_large():
    assert pythondemo.factorial(10) == 3628800

@pytest.mark.parametrize("n,result", [
    (1, 1),
    (3, 6),
    (5, 120),
    (7, 5040)
])
def test_factorial_param(n, result):
    assert pythondemo.factorial(n) == result