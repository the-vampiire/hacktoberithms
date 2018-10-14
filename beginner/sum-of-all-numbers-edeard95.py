A = [10,13,7]
B = [1,2,3,4,5,6]

def sum_all(A, B):
	ASum = sum(A)
	#print(ASum)
	BSum = sum(B)
	#print(BSum)
	TSum = ASum+BSum
	#print(TSum)
	
	return ASum, BSum, TSum
ASum, BSum, TSum = sum_all(A,B)
print('The sum of list 1 is '+str(ASum))
print('The sum of list 2 is '+str(BSum))
print('The sum of both lists is '+str(TSum))
