def calcular_area_circulo(radio):
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    area = 3.14159 * radio * radio
    return area

try:
    radio_ingresado = float(input("Ingrese el radio del círculo: "))
    area_calculada = calcular_area_circulo(radio_ingresado)
    print("El área del círculo con radio {} es: {:.2f}".format(radio_ingresado, area_calculada))
except ValueError as ve:
    print(ve)
    #.