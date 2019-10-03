def sum_earnings(input):
	A = input.split(',')
	B = []
	for i in A:
		B.append(float(i))
		if sum(B) < 0:
		B = []
	C = sum(B)
	earn = round(C, 2)
	#print(earn)
	return earn
out = sum_earnings(input('Add this month\'s earnings:'))
print(out)
