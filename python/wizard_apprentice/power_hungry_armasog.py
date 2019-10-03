def answer(xs):
	product = 1
	count_of_negatives = 0 # Tracking the amount of negative numbers as we need to multiply the result by the maximum even number of negative values
	for i in xs:
		if i < 0:
			count_of_negatives += 1
		if i > 1:
			product = product * i
	xs.sort()
	if count_of_negatives > 1:
		if count_of_negatives % 2 == 0:
			for j in range(count_of_negatives):
				product = product * xs[j]
		else:
			for j in range(count_of_negatives-1):
				product = product * xs[j]
	return str(product)


