from math import gcd


class Rational:
    def __init__(self, numerator, denominator):
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common



if __name__ == "__main__":
    r1 = Rational(1, 2)
    r2 = Rational(3, 5)

    assert r1 + r2 == Rational(11, 10)           # 11/10
    assert Rational(2, 3) + 7 == Rational(23, 3) # 23/3
    assert 7 + Rational(2, 3) == Rational(23, 3) # 23/3