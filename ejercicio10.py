'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''


def calcular_potencia(base, exponente):
    resultado = 1.0  # Inicializamos el resultado en 1

    for _ in range(exponente):  # Repetimos la multiplicación 'exponente' veces
        resultado *= base  # Multiplicamos el resultado por la base

    return resultado

# Solicitar al  usuario la base y el exponente
base = float(input("Introduce un número real (base): "))
exponente = int(input("Introduce un número entero positivo (exponente): "))

# Validar que el exponente sea positivo
if exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    # Calcular y mostrar el resultado
    resultado = calcular_potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado}")