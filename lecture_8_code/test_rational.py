# test_rational.py
import sys
sys.dont_write_bytecode = True # dont write pyc files to cache and disk
import pytest
from rational import Rational


def test_rational_sum():
    s = Rational(0, 1)
    for _ in range(10):
        s = s + Rational(1, 10)

    assert s.numerator == 1
    assert s.denominator == 1


def test_init_simplify():
    r = Rational(2, 4)
    assert r.numerator == 1
    assert r.denominator == 2


def test_init_negative_denominator():
    r = Rational(1, -3)
    assert r.numerator == -1
    assert r.denominator == 3


def test_init_zero_numerator():
    r = Rational(0, 5)
    assert r.numerator == 0
    assert r.denominator == 1  # canonical form


def test_zero_denominator_raises():
    with pytest.raises(ValueError):
        Rational(1, 0)


def test_add_rationals():
    a = Rational(1, 2)
    b = Rational(1, 3)
    c = a + b
    assert c.numerator == 5
    assert c.denominator == 6


def test_add_integer():
    a = Rational(3, 4)
    c = a + 1
    assert c.numerator == 7
    assert c.denominator == 4


def test_add_commutative():  # needs __eq__
    a = Rational(2, 5)
    b = Rational(3, 5)
    assert a + b == b + a