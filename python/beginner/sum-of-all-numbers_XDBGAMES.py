def sum_all():
	result=int(0)
	
	n1 = input("Inserta el primer numero: ")
	valor = False
	while True:	
		if n1.isdigit():
			valor=True
			n1=int(n1)
		if valor==True:
			if n1>0:
				break

	n2 = input("Inserta el segundo numero: ")
	valor = False
	while True:
		if n2.isdigit():
			valor=True
			n2=int(n2)
		if valor == True:
			if n2>0:
				break

	if n1<n2:
		fin=int(n2+1)
		cont=int(n1)
		n3=int(n1)
	else: 
		cont=int(n2)
		fin=int(n1+1)
		n3=int(n2)
	for cont in range (n3,fin):
		result=result+cont
	print (result)
	return result

print(sum_all())
input("pulse enter para salir")