class Rational:
	pass

def test_rational():
	r1 = Rational(1, 2)
	r2 = Rational(3, 4)
	assert r1 + r2 == Rational(5, 4)
	assert r1 * r2 == Rational(3, 8)
	assert r1 / r2 == Rational(2, 3)
	assert 2*r1 == Rational(1, 1)
	assert r1*2 == Rational(1, 1)
	assert r1 + 5 == Rational(11, 2)

if __name__ == "__main__":
	test_rational()
