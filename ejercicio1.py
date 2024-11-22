#Crea una programa que pida un número y calcule su factorial


# Pedir  un número 
numero = int(input("Introduce un número: "))

# Factorial
factorial = 1

# Se calcula el factorial
for i in range(1, numero + 1):
    factorial *= i

# Resultado
print(f"El factorial de: {numero} Es: {factorial}.")
