import math 
def CalcularInteres(precio, interes):
    return precio * interes
def CalcularPrecio(precio, ganancia):
    return precio + (ganancia * precio)
def precioVenta(precio, interes, ganancia):
    total = CalcularPrecio(precio, ganancia)
    interes = CalcularInteres(total, interes)
    return total + interes
interes = float(input("Ingrese el interes: "))
precio = float(input("Ingrese el precio: "))
ganancia = float(input("Ingrese la ganancia: "))
print(precioVenta(precio, interes, ganancia))