def count_char_freq(text):
	freq = {}
	for char in text:
		if char in freq:
			freq[char] += 1
		else:
			freq[char] = 1
	return freq


text = """Can you can a can as a canner can can a can?"""

char_freq = count_char_freq(text)
print(char_freq)
