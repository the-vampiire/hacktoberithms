def sum_all(l):
	start = int(l[0])
	end = int(l[1])
	sum=0
	for i in range(start,end+1):
		sum+=i
	return sum

a = int(input())
b = int(input())
input_list = sorted([a,b])
print(sum_all(input_list))