def sum_all(numbers):
	return sum(range(min(numbers), max(numbers)+1))

print sum_all([1,4])
print sum_all([100,1])