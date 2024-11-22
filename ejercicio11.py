'''
Escribe un programa que diga si un número introducido por teclado es o no primo. 
'''

import math

def es_primo(numero):
    # Los números menores o iguales a 1 no son primos
    if numero <= 1:
        return False
    # Verificamos divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False  # Si es divisible, no es primo
    return True  # Si no es divisible por ningún número, es primo

#  Introduzca un número
numero = int(input("Introduce un número entero: "))

# Comprobar si el número es primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")