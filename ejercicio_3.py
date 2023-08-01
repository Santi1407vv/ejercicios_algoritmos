import random

def generar_lista_aleatoria(longitud, minimo, maximo):
    lista_aleatoria = [random.randint(minimo, maximo) for _ in range(longitud)]
    return lista_aleatoria


try:
    longitud_lista = 10
    valor_minimo = 1
    valor_maximo = 100

    lista_aleatoria = generar_lista_aleatoria(longitud_lista, valor_minimo, valor_maximo)
    print("Lista de números aleatorios:", lista_aleatoria)
except ValueError as ve:
    print(ve)
    #.