'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''


def imprimir_numeros_pares():
    # Solicitar al usuario el primer número
    num1 = int(input("Introduce el primer número: "))
    # Solicitar al usuario el segundo número
    num2 = int(input("Introduce el segundo número: "))

    # Determinar el rango correcto
    if num1 > num2:
        num1, num2 = num2, num1  # Intercambiar si num1 es mayor que num2

    print(f"Números pares entre {num1} y {num2}:")

    # Imprimir los números pares en el rango
    for numero in range(num1, num2 + 1):
        if numero % 2 == 0:  # Verificar si el número es par
            print(numero)

# Ejecutar la función
imprimir_numeros_pares()