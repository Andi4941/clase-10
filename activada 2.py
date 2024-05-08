# Solicitar al usuario la cantidad de bultos
cantidad_bultos = int(input("Ingrese la cantidad de bultos: "))

# Inicializar la variable de número de bulto en 1
nro_bulto = 1

# Inicializar la variable para almacenar el total de peso
total_peso = 0

# Inicializar la variable para almacenar el peso máximo
peso_maximo = 50

# Mientras el número de bulto sea menor o igual a la cantidad de bultos ingresados por el usuario
while nro_bulto <= cantidad_bultos:
    # Solicitar al usuario el peso del bulto
    peso_bulto = float(input(f"Ingrese el peso del bulto {nro_bulto}: "))
    
    # Validar que el peso del bulto sea positivo
    while peso_bulto <= 0:
        print("Error: El peso del bulto debe ser mayor que cero.")
        peso_bulto = float(input(f"Ingrese el peso del bulto {nro_bulto}: "))
    
    # Verificar si el peso del bulto excede el peso máximo
    if peso_bulto > peso_maximo:
        print(f"El bulto {nro_bulto} excede el peso máximo permitido.")
    else:
        total_peso += peso_bulto
    
    # Incrementar el número de bulto
    nro_bulto += 1

# Mostrar el total de peso de los bultos ingresados
print(f"El peso total de los {cantidad_bultos} bultos es: {total_peso}")