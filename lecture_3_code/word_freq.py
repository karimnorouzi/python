def count_word_freq(text):
	freq = {}
	words = text.split()
	for word in words:
		if word in freq:
			freq[word] += 1
		else:
			freq[word] = 1
	return freq

text = """Can you can a can as a canner can can a can?"""
word_freq = count_word_freq(text)
print(word_freq)
