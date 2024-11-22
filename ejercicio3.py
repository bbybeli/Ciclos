#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
#y la media de todos los números introducidos.
def calcular_suma_y_media():
    suma = 0  # Acumulador para la suma de los números
    contador = 0  # Contador para la cantidad de números introducidos

    while True:
        numero = float(input("Introduce un número (0 para terminar): "))  # Solicita un número al usuario

        if numero == 0:  
            break

        suma += numero  # Acumula el número en la suma
        contador += 1  # Incrementa el contador

    
    if contador > 0:
        media = suma / contador  # Calcula la media
        print(f"La suma de los números introducidos es: {suma}")
        print(f"La media de los números introducidos es: {media}")
    else:
        print("No se introdujeron números.")

# Ejecutar la función
calcular_suma_y_media()