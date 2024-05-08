try:
    # Solicitar al usuario dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar la división
    resultado = num1 / num2

    # Mostrar el resultado
    print("El resultado de la división es:", resultado)

except ValueError:
    # Capturar el error si se ingresa un valor no numérico
    print("Error: Debe ingresar valores numéricos.")

except ZeroDivisionError:
    # Capturar el error si se intenta dividir por cero
    print("Error: No se puede dividir por cero.")