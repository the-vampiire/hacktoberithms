def mutations(input_list):
	print input_list[0],input_list[1]
	first = list(input_list[0].lower())
	second = list(input_list[1].lower())

	try:
		for ele in second:
			first.remove(ele)

	except:
		return False

	return True


print mutations(["hello","heel"])
print mutations(["Alien","line"])
