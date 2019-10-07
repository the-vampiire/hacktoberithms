def sum_all(n1,n2):
    aux = 0

    if n1 >= n2:
        aux = n2
        n2 = n1
        n1 = aux

    acum = 0
    i = n1
    while i<=n2:
        acum = acum+i
        i = i + 1

    if n1 == n2:
        acum=n1+n2

    return(str(acum))        

valor_valido = False

while True:
    num1 = input("Escribe el primer numero:")

    if num1.isdigit():
            valor_valido = True
            num1 = int(num1)

    if valor_valido == True:
        if num1>0:
            break

valor_valido = False

while True:
    num2 = input("Escribe el segundo numero:")

    if num2.isdigit():
        valor_valido = True
        num2 = int(num2)

    if valor_valido == True:
        if num2>0:
            break

print("La suma es: "+sum_all(num1, num2))
input("Pulse enter para salir")