from math import gcd


class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        if numerator == 0:
            self.numerator = 0
            self.denominator = 1
            return

        # Normalize sign so denominator is always positive
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __add__(self, other):
        if isinstance(other, Rational):
            new_numerator = (
                self.numerator * other.denominator
                + other.numerator * self.denominator
            )
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)

        elif isinstance(other, int):
            new_numerator = self.numerator + other * self.denominator
            return Rational(new_numerator, self.denominator)

        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __eq__(self, other):
        if isinstance(other, Rational):
            return (
                self.numerator == other.numerator
                and self.denominator == other.denominator
            )
        return False

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"


if __name__ == "__main__":
    r1 = Rational(1, 2)
    r2 = Rational(3, 5)

    print(r1 + r2)           # 11/10
    print(Rational(2, 3) + 7) # 23/3
    print(7 + Rational(2, 3)) # 23/3