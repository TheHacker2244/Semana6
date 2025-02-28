numero = input("Ingresa un número: ")
if numero.isdigit():  
    suma = 0
    for digito in numero:
        suma += int(digito)
    print(f"La suma de los dígitos de {numero} es: {suma}")
else:
    print("Por favor, ingresa un número válido.")