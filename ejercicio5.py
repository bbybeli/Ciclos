#Programa que pida 10 números e imprima el promedio de estos.

# Inicializar el acumulador y el contador
suma = 0
contador = 0

# Solicitar 10 números al usuario
for _ in range(10):
    numero = float(input("Introduce un número: "))
    suma += numero
    contador += 1

# Calcular el promedio
promedio = suma / contador

# Imprimir el promedio
print(f"El promedio de los números introducidos es: {promedio}")