#ejercicio de la circunferencia
import math
def calcular_circunferencia(radio):
  circunferencia = 2 * math.pi * radio
  return circunferencia
radio = 8
circunferencia = calcular_circunferencia(radio)
print(f"La circunferencia de un círculo con radio {radio} es: {circunferencia}") 