# Actualizar el conversor de moneda
# Creen un menu donde se muestre 3 opciones para que el usuario pueda elegir entre convertir de pesos chilenos, argentinos o mexicanos a dolares.
# peso_mexicano = 17 peso_chileno = 797 peso_argentino = 263

def conversor_moneda(valor_dolar):
    pesos = int(input("Ingrese pesos a convertir: "))

    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)

    print("Usted tiene $" + str(dolares) + " dólares")

print("""
Convertidor de moneda:
      1 - Peso chileno a dolar
      2 - Peso mexicano a dolar
      3 - Peso argentino a dolar
""")
opcion = int( input("Ingrese una opción: ") )

if opcion == 1:
    conversor_moneda(797)
elif opcion == 2:
    conversor_moneda(17)
elif opcion == 3:
    conversor_moneda(263)
else:
    print("Opción ingresa no valida")