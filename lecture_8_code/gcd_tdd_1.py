def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def test_gcd():
	assert gcd(48, 18) == 6
	assert gcd(56, 98) == 14
	assert gcd(98, 56) == 14
	assert gcd(12, 15) == 3
	assert gcd(7, 1)  == 1

if __name__ == "__main__":
	test_gcd()	
