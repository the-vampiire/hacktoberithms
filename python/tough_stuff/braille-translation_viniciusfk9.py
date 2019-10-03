# Braille Lower case mapping
BRAILLE_LOWER = [
			"100000", # a
            "110000", # b
            "100100", # c
            "100110", # d
            "100010", # e
            "110100", # f
            "110110", # g
            "110010", # h
            "010100", # i
            "010110", # j
            "101000", # k
            "111000", # l
            "101100", # m
            "101110", # n
            "101010", # o
            "111100", # p
            "111110", # q
            "111010", # r
            "011100", # s
            "011110", # t
            "101001", # u
            "111001", # v
            "010111", # w
            "101101", # x
            "101111", # y
			"101011",  # z
			"000000" # ' '
		] 
# Braille Upper case mapping
BRAILLE_UPPER = list(map(lambda x:'000001'+x, BRAILLE_LOWER[:-1]))

def ascii_to_braille(text):
	# Alphabet
	intab = b"abcdefghijklmnopqrstuvwxyz "

	# Mapping lower case -> (letter, braille(letter))
	d_lower = dict(zip(intab, BRAILLE_LOWER))
	
	# Mapping Upper case -> (letter, braille(letter))
	d_upper = dict(zip(intab.upper(), BRAILLE_UPPER))

	# Full Mapping = Lower Case + Upper Case
	mapping = dict(d_lower)
	mapping.update(d_upper)

	trantab = str.maketrans(mapping) # Translation Table
	translated_text = text.translate(trantab) # Translates the text using the table

	return translated_text

if __name__ == '__main__':
	# Test Cases
	tests = [
		'code',
		'Braille',
		'The quick brown fox jumped over the lazy dog',
		'Hello World'
	]

	for t in tests:
		print('{0} -> {1}'.format(t, ascii_to_braille(t)))
