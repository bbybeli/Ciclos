'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''



# Inicializar variables
ahorros_totales = 0
ahorros_mensuales = []

# Solicitar los depósitos mensuales al usuario
for mes in range(1, 13):
    deposito = float(input(f"Introduce el depósito para el mes {mes}: "))
    ahorros_totales += deposito
    ahorros_mensuales.append(ahorros_totales)

# Mostrar los ahorros acumulados cada mes
for mes, ahorro in enumerate(ahorros_mensuales, start=1):
    print(f"Ahorros al final del mes {mes}: {ahorro:.2f}")

# Mostrar el total ahorrado al final del año
print(f"Total ahorrado al final del año: {ahorros_totales:.2f}")