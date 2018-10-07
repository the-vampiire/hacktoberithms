# This function returns true if the string in the first element of the list contains all of the letters of the second element of the list
# Repeat letters only count once. For example, if a letter occurs twice in the second element than it must occur twice in the first element. 

def mutations(words):
	first = list(words[0])
	second = list(words[1])
	first_count = {}
	second_count = {}
	for c in first:
		if c in first_count:
			first_count[c] += 1
		else:
			first_count[c] = 1
	for c in second:
		if c in second_count:
			second_count[c] += 1
		else:
			second_count[c] = 1
	for key in second_count:
		try:
			if second_count[key] > first_count[key]:
				return False
				break
		except KeyError:
			return False
			break
	else:
		return True 



