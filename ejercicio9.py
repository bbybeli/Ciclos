#Escribe un programa que pida el limite inferior y superior de un intervalo. 



def intervalo_numeros():
    # Solicitar límites del intervalo
    while True:
        limite_inferior = int(input("Introduce el límite inferior: "))
        limite_superior = int(input("Introduce el límite superior: "))
        
        if limite_inferior < limite_superior:
            break  
        else:
            print("El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")

    suma_intervalo = 0
    fuera_intervalo = 0
    limites_ingresados = False

    print("Introduce números (introduce 0 para terminar):")
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break 
        
        # Verificar si el número está dentro del intervalo
        if limite_inferior < numero < limite_superior:
            suma_intervalo += numero  # Sumar si está dentro del intervalo
        else:
            fuera_intervalo += 1  # Contar si está fuera del intervalo
        
        # Verificar si el número es igual a los límites
        if numero == limite_inferior or numero == limite_superior:
            limites_ingresados = True

    # Mostrar resultados
    print(f"La suma de los números dentro del intervalo ({limite_inferior}, {limite_superior}) es: {suma_intervalo}")
    print(f"Números fuera del intervalo: {fuera_intervalo}")
    if limites_ingresados:
        print("Se introdujo al menos un número igual a los límites del intervalo.")
    else:
        print("No se introdujo ningún número igual a los límites del intervalo.")

# Ejecutar la función
intervalo_numeros()


