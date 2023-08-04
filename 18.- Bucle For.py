# Bucle for

print( range(10) )
# range(inicio, fin, pasos)

print( list(range(2,10, 2)) )

for contador in range(1, 11):
    print( contador )

lista = [1,2,3,4,5]
for l in lista:
    print(l)

diccionario = {
    "Pais": "Chile",
    "Capital": "Santiago",
    "Poblacion": 20000000
}
for llave in diccionario:
    print(llave)
    print(diccionario[llave])

for llave, valor in diccionario.items():
    print(llave)
    print(valor)
    print("-----")