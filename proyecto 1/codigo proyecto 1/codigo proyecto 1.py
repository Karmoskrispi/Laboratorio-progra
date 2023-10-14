CODIGO = True

while CODIGO:
    print("bienvenido") 
    print("1. ingresar datos de linea")
    print("2. salir")
    lineas = int(input("ingrese una opcion: "))

    if lineas == 2:
        print("hasta luego")
        CODIGO = False
    elif lineas > 2 or lineas < 0:
        print("ingrese una opcion valida")

    elif lineas == 1: 
        preciomt2 = print(int(input("ingrese precio por metro cuadrado: "))) 
        cantidadmt2 = print(int(input("ingrese cantidad de metros cuadrados vendidos en el mes: ")))
        cantidad = int(input("Ingrese cantidad de empleados (1-20): "))
        empleados = []
        ganancia_total = 0
        while True:
            if 1 <= cantidad <= 20:
                for _ in range(cantidad):
                    costodehora = float(input("Ingrese costo de la hora del empleado: "))
                    horas = int(input("Ingrese cantidad de horas trabajadas: "))
                    salario = costodehora * horas
                    empleado = {
                         "costo de hora": costodehora,
                         "horas": horas,
                        "salario": salario
                        }
                    empleados.append(empleado)
                    break
                else:
                    print("Ingrese una cantidad de empleados válida (1-20)")

            print("\nInformación de los empleados:")
            for empleado in empleados:
                print("Costo de hora:", empleado)
                print("Horas trabajadas:", empleado)
                print("Salario:", empleado)
                print()
                ganancia_total += empleado["salario"]

           