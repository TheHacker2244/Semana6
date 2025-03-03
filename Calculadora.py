def calculadora():
    print("Calculadora Básica")
    print("Seleccione una operación")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opción = input("Ingrese el número de la operación deseada:")
    if opción in ('1', '2', '3', '4',):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el Segundo número: "))
        if opción == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opción == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opción == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opción =='4':
            if num2 !=0:
                print("Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Eror: No se puede dividir por cero.")
    else:
        print("Opción no válida. Intente de nuevo.")
calculadora()