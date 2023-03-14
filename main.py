mayor = 0
residuo = 0
#1
n = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))
if n > n2:
    mayor = n
    print("Número mayor: ", mayor)
elif n2 > n:
    mayor = n2
    print("El número mayor es: ", mayor)
