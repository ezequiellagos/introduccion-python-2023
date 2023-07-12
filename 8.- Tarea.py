# Actualizar el conversor de moneda
# Creen un menu donde se muestre 3 opciones para que el usuario pueda elegir entre convertir de pesos chilenos, argentinos o mexicanos a dolares.
# peso_mexicano = 17 peso_chileno = 797 peso_argentino = 263

print("""
Convertidor de moneda:
      1 - Peso chileno a dolar
      2 - Peso mexicano a dolar
      3 - Peso argentino a dolar
""")
opcion = int( input("Ingrese una opción: ") )

if opcion == 1:
    pesos = int(input("Ingrese pesos chilenos a convertir: "))
    valor_dolar = 797

    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)

    print("Usted tiene $" + str(dolares) + " dólares")
elif opcion == 2:
    pesos = int(input("Ingrese pesos mexicanos a convertir: "))
    valor_dolar = 17

    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)

    print("Usted tiene $" + str(dolares) + " dólares")
elif opcion == 3:
    pesos = int(input("Ingrese pesos argentinos a convertir: "))
    valor_dolar = 263

    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)

    print("Usted tiene $" + str(dolares) + " dólares")
else:
    print("Opción ingresa no valida")