# Tipos de datos
# En Python todo es un objeto

# Tipos de datos
# 1.- Numeros enteros (int integer)
# 2.- Numeros decimales (float flotantes)
# 3.- Cadenas de texto (string str)
# 4.- Booleanos

# 1.- Numeros enteros
# 1 2 3 500 9000

# 2.- Numeros decimales
# 3.5 3.1416247874 4.0
decimal = 25.36

# 3.- Cadenas de texto
cadena_de_texto = "Esto es una 'cadena' de texto"
comillas_simples = 'esto es "otra" cadena de texto'
comillas_triples = """ "comillas dobles" 'comillas simples' 
aca iria mas informacion
sobre el curso
con python
"""
print(comillas_triples)

cadena_1 = "Hola"
cadena_2 = "Mundo"
print(cadena_1 + " " + cadena_2)

# 4.- Booleanos (True, False)
es_estudiante = True
trabaja = False

print(es_estudiante)
print(trabaja)

# Convertir tipos de datos
numero_1 = input("Ingrese un numero 1: ")
numero_2 = input("Ingrese un numero 2: ")

print(numero_1 + numero_2)
print( int(numero_1) + int(numero_2) )

decimal_2 = 125.12
print( int(decimal_2) )

numero_entero = 45
print( float(numero_entero) )

print("El numero entero es: " + str(numero_entero))