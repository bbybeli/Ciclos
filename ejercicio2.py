
#Crea un programa que permita adivinar un número
import random

def adivinar_numero():
    numero_aleatorio = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    intentos_maximos = 10
    intentos_realizados = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 100. Tienes 10 intentos para adivinarlo.")

    while intentos_realizados < intentos_maximos:
        intento = int(input("Introduce tu intento: "))
        intentos_realizados += 1

        if intento < numero_aleatorio:
            print("El número a adivinar es mayor que", intento)
        elif intento > numero_aleatorio:
            print("El número a adivinar es menor que", intento)
        else:
            print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intentos_realizados} intentos.")
            break

        intentos_restantes = intentos_maximos - intentos_realizados
        if intentos_restantes > 0:
            print(f"Te quedan {intentos_restantes} intentos.")
        else:
            print(f"Lo siento, has agotado tus intentos. El número era {numero_aleatorio}.")

# Ejecutar el juego
adivinar_numero()