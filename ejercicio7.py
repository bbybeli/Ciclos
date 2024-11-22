'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
def verificar_vocales():

    while True:  

        caracter = input("Introduce un carácter (o espacio para terminar): ")  # Solicita un carácter


        

        if caracter == " ":

            print("Programa terminado.")

            break  


        # Verificar si el carácter es una vocal

        if caracter.lower() in 'aeiou':  # Comprueba si es una vocal

            print("VOCAL")

        else:

            print("NO VOCAL")


# Ejecutar la función

verificar_vocales()