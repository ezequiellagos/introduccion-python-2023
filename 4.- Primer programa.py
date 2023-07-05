# Conversor de moneda
# Transformar pesos chilenos a dólares. El programa debe pedir una catidad de pesos y mostrar el resultado en dolares.
# Valor del dolar: 797,33 CLP

pesos = int(input("Ingrese pesos chilenos a convertir: "))
valor_dolar = 797

dolares = pesos / valor_dolar
dolares = round(dolares, 2)

print("Usted tiene $" + str(dolares) + " dólares")