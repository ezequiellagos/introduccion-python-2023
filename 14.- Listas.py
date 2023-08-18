# Listas

# Las listas son un tipo de dato que nos permite almacenar varios valores.
# Las listas se definen con corchetes cuadrados [] y cada elemento se separa por una coma

lista = [1,2,3,4,5]

lista2 = [1, "hola", 5.1, True, [1,2,3]]
lista_2 = [
    1,
    "hola",
    5.1,
    True,
    [1,2,3]
]

# Las listas son mutables, es decir, que se pueden modificar

print(lista[0])
lista[0] = 6
print( lista )

# Determinar el largo de la lista
print( len(lista) )

# Agregar elemento
lista.append(6)
print(lista)

# Eliminar el ultimo elemento
lista.pop()
print(lista)

# Eliminar un elemento de la lista
lista.remove(2)
print(lista)

# Elimina todos los elementos de una lista
lista.clear()
print(lista)

# Cuantas veces se repite un elementos
lista3 = [1,1,2,3,4,5,5,5,6]
print( lista3.count(5) )

# Clase del 18-08-2023

nueva_lista_1 = [1,2,3]
nueva_lista_2 = [4,5,6]
print( type(nueva_lista_1) )

print(nueva_lista_1 + nueva_lista_2)
print(3 * nueva_lista_1)