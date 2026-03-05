def encrypt(text, cipher):
	return ''.join(cipher.get(char, char) for char in text)

cipher = {'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q','f': 'r', 'g': 's', 'h': 't', 'i': 'u', 'j': 'v','k': 'w', 'l': 'x', 'm': 'y', 'n': 'z', 'o': 'a',
			'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f','u': 'g', 'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k',
			'z': 'l'}

original_text = "hello, this is super secret. see in location x"
encrypted_text = encrypt(original_text, cipher)
print(encrypted_text)  # Output: "tqxxa"
# decrytpion is just applying the same function with the same cipher
# invert the key items in the cipher to get the decryption cipher
cipher = {v: k for k, v in cipher.items()}
plain_text = encrypt(encrypted_text, cipher)
print(plain_text)  # Output: "hello"


# using these tricks:
#cgen = (c for c in "this is a test")
#next(cgen)

# '-'.join("this is a test") output:'t-h-i-s- -i-s- -a- -t-e-s-t'