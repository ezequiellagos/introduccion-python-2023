# Diccionarios

# Son una colección que se utiliza para almacenar valores que tienen una relación entre si
# Los diccionarios se definen con llaves {} y cada elemento se separa por una coma

diccionario = {
    "nombre": "Luigi",
    "apellido": "Bross",
    "apodo": "Mario Verde",
    "edad": 25,
    "es_verde": True,
    "estatura": 1.5
}

print( diccionario["nombre"] )

print( len(diccionario) )

# Metodo para obtener el valor de un elemento
print( diccionario.get("nombre") )

# Elimina un elemento
print( diccionario )
diccionario.pop("apodo")
print( diccionario )

# Modificar un elemento
diccionario["nombre"] = "Mario"
diccionario.update({"apellido": "Castañeda"})
print(diccionario)

# Obtener lista de las llaves/claves/indices
print( diccionario.keys() )

# Obtener lista de los valores
print( diccionario.values() )

print( diccionario )
#diccionario.clear()
#diccionario.popitem()
print( diccionario )

