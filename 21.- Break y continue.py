# Break y Continue

def main():
    # Imprimir los numeros impares hasta el numero 1000
    for numero in range(1, 1000 + 1):
        if numero % 2 == 0:
            continue
        #print(numero)

    for numero in range(1000):
        #print(numero)
        if numero == 500:
            break

    texto = input("Ingrese una palabra: ")
    for letra in texto:
        if letra == 'a':
            break
        print(letra)


if __name__ == '__main__':
    main()