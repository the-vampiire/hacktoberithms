def sum_all(l):
	try:
		if len(l) > 2 or len(l) is 0:
			raise ValueError('List must have only 2 number exactly')
		if l[0] == l[1]:
			return int(l[0]) + int(l[1])
		else:
			if(l[0]<l[1]):
				return int(sum(range(l[0], l[1]+1)))
			else:
				return int(sum(range(l[1], l[0]+1)))
	except Exception as e:
		print(e.args)
