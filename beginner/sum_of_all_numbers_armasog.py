# Returns the sum of two numbers plus the sum of all numbers between them

def sum_all(n):
	between = []
	smaller = min(n)
	bigger = max(n)
	for n in range(smaller+1, bigger):
		between.append(n)
	solution = sum(between) + smaller + bigger
	return solution
