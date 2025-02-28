numero = int(input("Ingresa un número el cual quieras ver su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")