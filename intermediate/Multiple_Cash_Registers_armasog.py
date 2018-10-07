def checkout_time(customers, registers):
	tills = {}
	if registers == 1:
		return sum(customers)
	if len(customers) <= registers:
		return max(customers)
	for i in range(1, registers+1):
		tills[i] = customers[i]
	for j in range(registers, len(customers)):
		next_open = min(tills, key=tills.get)
		tills[next_open] += customers[j]
	return max(tills.values())


