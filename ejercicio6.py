#Realizar un algoritmo que pida números

# Solicitar una cantidad de números al usuario e informar cuántos son mayores, menores e iguales a 0

def contar_numeros(cantidad):
    mayores = 0
    menores = 0
    iguales = 0

    for i in range(cantidad):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        if numero > 0:
            mayores += 1
        elif numero < 0:
            menores += 1
        else:
            iguales += 1

    return mayores, menores, iguales

# Solicitar la cantidad de números a introducir
cantidad = int(input("Ingrese la cantidad de números a introducir: "))

# Contar y mostrar los resultados
mayores, menores, iguales = contar_numeros(cantidad)
print(f"Cantidad de números mayores que 0: {mayores}")
print(f"Cantidad de números menores que 0: {menores}")
print(f"Cantidad de números iguales a 0: {iguales}")
