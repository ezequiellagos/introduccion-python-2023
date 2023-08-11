#Escribe un programa que le pida al usuario un número ( n ) y calcule la suma de todos los números desde 1 hasta ( n ) usando un ciclo for.

numero = int( input("Ingrese un numero: ") )
suma = 0
for n in range(1, numero + 1):
    suma = suma + n

print(suma)