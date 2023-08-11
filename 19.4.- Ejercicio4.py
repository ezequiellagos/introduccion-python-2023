# Cree una calculadora, que muestre un menu de opciones (sumar, restar, multiplicar y dividir deben ser funciones que retornen el resultado) mientras no se le especifique que termine el programa. La calculadora debe pedir 2 numeros cada vez.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def main():
    mensaje = """
Calculadora
1) Suma
2) Resta
3) Multiplicación
4) División
5) Salir
"""
    print(mensaje)
    opcion = int( input("Ingrese una opción: ") )
    while opcion != 5:
        numero_1 = int( input("Ingrese numero 1: ") )
        numero_2 = int( input("Ingrese numero 2: ") )

        if opcion == 1:
            resultado = suma(numero_1, numero_2)
        elif opcion == 2:
            resultado = resta(numero_1, numero_2)
        elif opcion == 3:
            resultado = multiplicacion(numero_1, numero_2)
        elif opcion == 4:
            resultado = division(numero_1, numero_2)
        else:
            resultado = ""
            print("La opción ingresada no es válida")
        
        print(f"El resultado de la operación es: {resultado}")

        print(mensaje)
        opcion = int( input("Ingrese una opción: ") )

if __name__ == "__main__":
    main()