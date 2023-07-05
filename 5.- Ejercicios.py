# Ejercicio 1
# Escribir un programa que pregunte el nombre al usuario y un numero entero. Imprima por consola el nombre del usuario, uno por linea, tantas veces como el numero introducido.

# print("Hola" * 3)

#nombre = input("Ingrese nombre: ")
#numero = int(input("Ingrese un numero: "))

#print( (nombre + "\n") * numero)

# Ejercicio 2
# Escribir por pantalla el resultado de la siguiente opercion aritmetica: 


# Ejercicio 3
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = 112
peso_muneca = 75

payasos_vendidos = int(input("Ingrese cantidad payasos vendidos: "))
munecas_vendidas = int(input("Ingrese cantidad muñecas vendidas: "))

peso_total = (payasos_vendidos * peso_payaso) + (munecas_vendidas * peso_muneca)

print("El peso total del paquete son: " + str(peso_total) + " gramos")

#Ejercicio 4
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase "Tu índice de masa corporal es <imc>", donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.