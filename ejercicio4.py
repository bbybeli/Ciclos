
#Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

def mostrar_tablas_multiplicar():
    for i in range(1, 6):  
        print(f"Tabla de multiplicar del {i}:")
        for j in range(1, 11):  
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print()

# Ejecutar la función
mostrar_tablas_multiplicar()