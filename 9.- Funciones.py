# Funciones

print("Reaprendiendo Python")
print("Reaprendiendo Python")
print("Reaprendiendo Python")
print("Reaprendiendo Python")

# Nombres de las funciones siguen las mismas reglas que el de las variables
def imprimir_mensaje():
    print("Reaprendiendo Python")
    print("Hola")

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

print("Hola Juan")
print("Hola Pedro")

def saludo(nombre = "Juan", apellido = "Perez"):
    print("Hola " + nombre + " " + apellido)

saludo()
saludo("Pedro")
saludo("Matias", "Aguilera")
saludo(apellido="Lagos", nombre="Ezequiel")
saludo(apellido="Castillo")