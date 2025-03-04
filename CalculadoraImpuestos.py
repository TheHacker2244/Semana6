print("Bienvenido proporciona los precios, ganancia y impuestos")
precio = input("ingrese el precio: ")
precio = float(precio)
ganancia = input("ingrese la ganancia: ")
ganancia = float(ganancia)
impuesto = input("ingrese el impuesto: ")
impuesto = float(impuesto)
def calcularImpuesto(impuesto, precio):
    return impuesto * precio
def calcularGanancia(ganancia, precio):
    return ganancia * precio
def calcularPrecioFinal(precio, impuesto, ganancia):
    precio1 = calcularGanancia(ganancia, precio,) + precio
    impuestoVenta = calcularImpuesto(impuesto, precio1)
    return precio1 + impuestoVenta
print(calcularPrecioFinal(precio, impuesto, ganancia))