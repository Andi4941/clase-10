try:
    cantidad_bultos = int(input("Ingrese la cantidad de bultos: "))
    if cantidad_bultos <= 0:
        raise ValueError("La cantidad de bultos debe ser mayor que cero")
except ValueError as ve:
    print("Error:", ve)
    exit()

total_pagar = 0
bultos_livianos = 0
bultos_normales = 0

for _ in range(cantidad_bultos):
    while True:
        try:
            peso = float(input("Ingrese el peso del bulto: "))
            if peso < 0:
                raise ValueError("El peso del bulto no puede ser negativo")
            break
        except ValueError as ve:
            print("Error:", ve)

    if peso >= 1 and peso <= 5:
        total_pagar += 1000
        bultos_livianos += 1
    elif peso > 5 and peso <= 10:
        total_pagar += 2000
        bultos_normales += 1
    else:
        print("El peso del bulto no corresponde a ninguna categoría")

print(f"{bultos_livianos} bultos livianos ${bultos_livianos * 1000}")
print(f"{bultos_normales} bultos normales ${bultos_normales * 2000}")
print(f"Valor total a pagar: ${total_pagar}")