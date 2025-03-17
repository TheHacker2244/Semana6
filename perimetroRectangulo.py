def perimetro_rectangulo(base, altura):
  if base <= 0 or altura <= 0:
    raise ValueError("La base y la altura deben ser valores positivos no Negativos ni Cero.")
  return 2 * (base + altura)
base = 2
altura = 10
perimetro = perimetro_rectangulo(base, altura)
print(f"El perímetro del rectángulo es: {perimetro}")