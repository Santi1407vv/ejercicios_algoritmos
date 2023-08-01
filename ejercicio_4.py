def es_par(numero):
    return numero % 2 == 0

try:
    numero_ingresado = int(input("Ingrese un número entero: "))
    if es_par(numero_ingresado):
        print("El número {} es par.".format(numero_ingresado))
    else:
        print("El número {} es impar.".format(numero_ingresado))
except ValueError as ve:
    print("Error: Ingrese un número entero válido.")