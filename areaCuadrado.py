 #Aquí se calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    return lado * lado

# Aquí se Solicitar al usuario la longitud del lado del cuadrado
lado = float(input("Introduce la longitud del lado del cuadrado: "))

#En estáparte se Calcular el área
area = calcular_area_cuadrado(lado)

#Y finalmente aquí se Mostrará el resultado
print(f"El área del cuadrado es: {area} unidades cuadradas.")
