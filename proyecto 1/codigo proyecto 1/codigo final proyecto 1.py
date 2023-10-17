CODIGO = True

while CODIGO:
    print("bienvenido") 
    print("1. comparacion de dos lineas")
    print("2. comparacion de tres lineas")
    print("3. comparación de las cuatro lineas")
    print("4. salir")
    lineas = int(input("ingrese una opcion: "))

#el usuario ingresara la opcion qque desea 
    if lineas == 4:
        print("hasta luego")
        CODIGO = False
    elif lineas > 4 or lineas < 0:
        print("ingrese una opcion valida")

#aqui ingresara las variables de la linea que desee 
    elif lineas == 1: 
        linea1 = input("ingrese numero de linea: ")
        preciomt2 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt2 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))

#aqui ingresara la informacion de cada uno de los empleados por separado 
        empleados = []
        costo_total = 0
        cantidad1 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad1 <= 20:
            for _ in range(cantidad1):
                numero_empleado = int(input("empleado No: "))
                costodehora = float(input("Ingrese costo de la hora del empleado: "))
                horas = int(input("Ingrese cantidad de horas trabajadas: "))
                salario = costodehora * horas
                empleado = {
                    "numero de empleado": numero_empleado,
                    "costo de hora": costodehora,
                    "horas": horas,
                    "salario": salario
                }
                empleados.append(empleado)
            print("\nInformación del empleado:")
            for empleado in empleados:
                print("Empleado No:", empleado["numero de empleado"])
                print("Costo de hora:", empleado["costo de hora"])
                print("Horas trabajadas:", empleado["horas"])
                print("Salario:", empleado["salario"])
                print()
                costo_total += empleado["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")

#se solicita la informacion de la segunda linea 
        linea2 = input("ingrese numero de linea: ")
        preciomt22 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt22 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))
        empleados2 = []
        costo_total2 = 0
        cantidad2 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad2 <= 20:
            for _ in range(cantidad2):
                numero_empleado2 = int(input("empleado No: "))
                costodehora2 = float(input("Ingrese costo de la hora del empleado: "))
                horas2 = int(input("Ingrese cantidad de horas trabajadas: "))
                salario2 = costodehora2 * horas2
                empleado2 = {
                    "numero de empleado": numero_empleado2,
                    "costo de hora": costodehora2,
                    "horas": horas2,
                    "salario": salario2
                }
                empleados2.append(empleado2)
            print("\nInformación de los empleados:")
            for empleado2 in empleados2: 
                print("Empleado No:", empleado2["numero de empleado"])
                print("Costo de hora:", empleado2["costo de hora"])
                print("Horas trabajadas:", empleado2["horas"])
                print("Salario:", empleado2["salario"])
                print()
                costo_total2 += empleado2["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")

#ingresara la opcion que desee obtener junto a la opcion de realizar otra comparacion 
        opciones = True
        while opciones:
            print("1. Ganancia Total")
            print("2. Costo Total")
            print("3. Ganancia Neta")
            print("4. indice de eficiencia")
            print("5. Comparaciion entre lineas")
            print("6. Realizar comparacion de otras lineas")
            x = int(input("Ingrese la opcion que desea obtener: "))
            #Ganancia total
            gananciatotal1 = preciomt2 * cantidadmt2
            gananciatotal2= preciomt22 * cantidadmt22
            #Ganancia Neta
            ganancianeta1 = gananciatotal1 - costo_total
            ganancianeta2 = gananciatotal2 - costo_total2
            #Indice de eficiencia
            indice1 = ganancianeta1/cantidad1
            indice2 = ganancianeta2/cantidad2
#aqui mostrara los calculos solicitados segun la opcion que haya escogido el usuario 

            if x == 1: 
                print("La Ganancia Total de la linea", linea1, "fue de", gananciatotal1)
                print("La Ganancia Total de la linea", linea2, "fue de", gananciatotal2)
            elif x== 2:
                print("El costo total de la linea", linea1, "fue de", costo_total )
                print("El costo total de la liinea", linea2, "fue de", costo_total2)
            elif x== 3: 
                print("La Ganancia Neta de la linea", linea1, "fue de", ganancianeta1 )
                print("La Ganancia Neta de la linea", linea2, "fue de", ganancianeta2 )
            elif x== 4: 
                print("El indice de eficiencia de la linea", linea1, "fue de", indice1)
                print("El indice de eficiencia de la linea", linea2, "fue de", indice2)
            elif x== 5: 
                if indice1 > indice2: 
                    print("La linea", linea1, "tuvo un mayor indice de eficiencia")
                else:
                    indice2 > indice1
                    print("La linea", linea2, "tuvo un mayor indice de eficiencia")
            elif x == 6:
                opciones = False   
            else: 
                print("ingrese una opcion valida") 
 
#se solicitara la informacion para tres lineas de produccion distintas para su debida comparacion 
    elif lineas == 2: 
        
        linea1 = input("ingrese numero de linea: ")
        preciomt2 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt2 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))
        empleados = []
        costo_total = 0
        cantidad1 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad1 <= 20:
            for _ in range(cantidad1):
                numero_empleado = int(input("empleado No: "))
                costodehora = float(input("Ingrese costo de la hora del empleado: "))
                horas = int(input("Ingrese cantidad de horas trabajadas: "))
                salario = costodehora * horas
                empleado = {
                    "numero de empleado": numero_empleado,
                    "costo de hora": costodehora,
                    "horas": horas,
                    "salario": salario
                }
                empleados.append(empleado)
            print("\nInformación de los empleados:")
            for empleado in empleados: 
                print("Empleado No:", empleado["numero de empleado"])
                print("Costo de hora:", empleado["costo de hora"])
                print("Horas trabajadas:", empleado["horas"])
                print("Salario:", empleado["salario"])
                print()
                costo_total += empleado["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")

        linea2 = input("ingrese numero de linea: ")
        preciomt22 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt22 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))
        empleados2 = []
        costo_total2 = 0
        cantidad2 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad2 <= 20:
            for _ in range(cantidad2):
                numero_empleado2 = int(input("empleado No: "))
                costodehora2 = float(input("Ingrese costo de la hora del empleado: "))
                horas2 = int(input("Ingrese cantidad de horas trabajadas: "))
                salario2 = costodehora2 * horas2
                empleado2 = {
                    "numero de empleado": numero_empleado2,
                    "costo de hora": costodehora2,
                    "horas": horas2,
                    "salario": salario2
                }
                empleados2.append(empleado2)
            print("\nInformación de los empleados:")
            for empleado2 in empleados2: 
                print("Empleado No:", empleado2["numero de empleado"])
                print("Costo de hora:", empleado2["costo de hora"])
                print("Horas trabajadas:", empleado2["horas"])
                print("Salario:", empleado2["salario"])
                print()
                costo_total2 += empleado2["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")
        
        linea3 = input("ingrese numero de linea: ")
        preciomt23 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt23 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))
        empleados3 = []
        costo_total3 = 0
        cantidad3 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad3 <= 20:
            for _ in range(cantidad3):
                numero_empleado3 = int(input("empleado No: "))
                costodehora3 = float(input("Ingrese costo de la hora del empleado: "))
                horas3 = int(input("Ingrese cantidad de horas trabajadas: "))
                salario3 = costodehora3 * horas3
                empleado3 = {
                    "numero de empleado": numero_empleado3,
                    "costo de hora": costodehora3,
                    "horas": horas3,
                    "salario": salario3
                }
                empleados3.append(empleado3)
            print("\nInformación de los empleados:")
            for empleado3 in empleados3: 
                print("Empleado No:", empleado3["numero de empleado"])
                print("Costo de hora:", empleado3["costo de hora"])
                print("Horas trabajadas:", empleado3["horas"])
                print("Salario:", empleado3["salario"])
                print()
                costo_total3 += empleado3["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")

        opciones2 = True
        while opciones2:
            print("1. Ganancia Total")
            print("2. Costo Total")
            print("3. Ganancia Neta")
            print("4. indice de eficiencia")
            print("5. Comparaciion entre lineas")
            x2 = int(input("Ingrese la opcion que desea obtener: "))
            #Ganancia total
            gananciatotal1 = preciomt2 * cantidadmt2
            gananciatotal2= preciomt22 * cantidadmt22
            gananciatotal3= preciomt23 * cantidadmt23
            #Ganancia Neta
            ganancianeta1 = gananciatotal1 - costo_total
            ganancianeta2 = gananciatotal2 - costo_total2
            ganancianeta3 = gananciatotal3 - costo_total3
            #Indice de eficiencia
            indice1 = ganancianeta1/cantidad1
            indice2 = ganancianeta2/cantidad2
            indice3 = ganancianeta3/cantidad3 

            if x2 == 1: 
                print("La Ganancia Total de la linea", linea1, "fue de", gananciatotal1)
                print("La Ganancia Total de la linea", linea2, "fue de", gananciatotal2)
                print("La Ganancia Total de la linea", linea3, "fue de", gananciatotal3)
            elif x2 == 2:
                print("El costo total de la linea", linea1, "fue de", costo_total )
                print("El costo total de la linea", linea2, "fue de", costo_total2)
                print("El costo total de la linea", linea3, "fue de", costo_total3)
            elif x2 == 3: 
                print("La Ganancia Neta de la linea", linea1, "fue de", ganancianeta1)
                print("La Ganancia Neta de la linea", linea2, "fue de", ganancianeta2)
                print("La Ganancia Neta de la linea", linea3, "fue de", ganancianeta3)

            elif x2 == 4: 
                print("El indice de eficiencia de la linea", linea1, "fue de", indice1)
                print("El indice de eficiencia de la linea", linea2, "fue de", indice2)
                print("El indice de eficiencia de la linea", linea3, "fue de", indice3)

            elif x2 == 5: 
                if indice1 > indice2 and indice1 > indice3: 
                    print("La linea", linea1, "tuvo un mayor indice de eficiencia")

                elif indice2 > indice1 and indice2 > indice3:
                    print("La linea", linea2, "tuvo un mayor indice de eficiencia")

                elif indice3 > indice1 and indice3 > indice2:
                    print("La linea", linea3, "tuvo un mayor indice de eficiencia")
            elif x2 == 6:
                opciones2 = False
                
            else: 
                print("ingrese una opcion valida")

#aqui solicitara informacion para las 4 lineas de produccion para su debida comparacion
    elif lineas == 3: 

        linea1 = input("ingrese numero de linea: ")
        preciomt2 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt2 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))
        empleados = []
        costo_total = 0
        cantidad1 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad1 <= 20:
            for _ in range(cantidad1):
                numero_empleado = int(input("empleado No: "))
                costodehora = float(input("Ingrese costo de la hora del empleado: "))
                horas = int(input("Ingrese cantidad de horas trabajadas: "))
                salario = costodehora * horas
                empleado = {
                    "numero de empleado": numero_empleado,
                    "costo de hora": costodehora,
                    "horas": horas,
                    "salario": salario
                }
                empleados.append(empleado)
            print("\nInformación de los empleados:")
            for empleado in empleados: 
                print("Empleado No:", empleado["numero de empleado"])
                print("Costo de hora:", empleado["costo de hora"])
                print("Horas trabajadas:", empleado["horas"])
                print("Salario:", empleado["salario"])
                print()
                costo_total += empleado["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")

        linea2 = input("ingrese numero de linea: ")
        preciomt22 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt22 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))
        empleados2 = []
        costo_total2 = 0
        cantidad2 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad2 <= 20:
            for _ in range(cantidad2):
                numero_empleado2 = int(input("empleado No: "))
                costodehora2 = float(input("Ingrese costo de la hora del empleado: "))
                horas2 = int(input("Ingrese cantidad de horas trabajadas: "))
                salario2 = costodehora2 * horas2
                empleado2 = {
                    "numero de empleado": numero_empleado2,
                    "costo de hora": costodehora2,
                    "horas": horas2,
                    "salario": salario2
                }
                empleados2.append(empleado2)
            print("\nInformación de los empleados:")
            for empleado2 in empleados2: 
                print("Empleado No:", empleado2["numero de empleado"])
                print("Costo de hora:", empleado2["costo de hora"])
                print("Horas trabajadas:", empleado2["horas"])
                print("Salario:", empleado2["salario"])
                print()
                costo_total2 += empleado2["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")
        
        linea3 = input("ingrese numero de linea: ")
        preciomt23 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt23 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))
        empleados3 = []
        costo_total3 = 0
        cantidad3 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad3 <= 20:
            for _ in range(cantidad3):
                numero_empleado3 = int(input("empleado No: "))
                costodehora3 = float(input("Ingrese costo de la hora del empleado: "))
                horas3 = int(input("Ingrese cantidad de horas trabajadas: "))
                salario3 = costodehora3 * horas3
                empleado3 = {
                    "numero de empleado": numero_empleado3,
                    "costo de hora": costodehora3,
                    "horas": horas3,
                    "salario": salario3
                }
                empleados3.append(empleado3)
            print("\nInformación de los empleados:")
            for empleado3 in empleados3: 
                print("Empleado No:", empleado3["numero de empleado"])
                print("Costo de hora:", empleado3["costo de hora"])
                print("Horas trabajadas:", empleado3["horas"])
                print("Salario:", empleado3["salario"])
                print()
                costo_total3 += empleado3["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")
        linea4 = input("ingrese numero de linea: ")
        preciomt24 = int(input("ingrese precio por metro cuadrado: "))
        cantidadmt24 = int(input("ingrese cantidad de metros cuadrados vendidos en el mes: "))
        empleados4 = []
        costo_total4 = 0
        cantidad4 = int(input("Ingrese cantidad de empleados (1-20): "))

        if 1 <= cantidad4 <= 20:
            for _ in range(cantidad4):
                numero_empleado4 = int(input("empleado No: "))
                costodehora4 = float(input("Ingrese costo de la hora del empleado: "))
                horas4 = int(input("Ingrese cantidad de horas trabajadas: "))
                salario4 = costodehora4 * horas4
                empleado4 = {
                    "numero de empleado": numero_empleado4,
                    "costo de hora": costodehora4,
                    "horas": horas4,
                    "salario": salario4
                }
                empleados4.append(empleado4)
            print("\nInformación de los empleados:")
            for empleado4 in empleados4: 
                print("Empleado No:", empleado4["numero de empleado"])
                print("Costo de hora:", empleado4["costo de hora"])
                print("Horas trabajadas:", empleado4["horas"])
                print("Salario:", empleado4["salario"])
                print()
                costo_total4 += empleado4["salario"]
        else:
            print("Ingrese una cantidad de empleados válida (1-20)")

        opciones3 = True
        while opciones3:
            print("1. Ganancia Total")
            print("2. Costo Total")
            print("3. Ganancia Neta")
            print("4. indice de eficiencia")
            print("5. Comparaciion entre lineas")
            x3 = int(input("Ingrese la opcion que desea obtener: "))
            #Ganancia total
            gananciatotal1 = preciomt2 * cantidadmt2
            gananciatotal2 = preciomt22 * cantidadmt22
            gananciatotal3 = preciomt23 * cantidadmt23
            gananciatotal4 = preciomt24 * cantidadmt24
            #Ganancia Neta
            ganancianeta1 = gananciatotal1 - costo_total
            ganancianeta2 = gananciatotal2 - costo_total2
            ganancianeta3 = gananciatotal3 - costo_total3
            ganancianeta4 = gananciatotal4 - costo_total4
            #Indice de eficiencia
            indice1 = ganancianeta1/cantidad1
            indice2 = ganancianeta2/cantidad2
            indice3 = ganancianeta3/cantidad3 
            indice4 = ganancianeta4/cantidad4 

            if x3 == 1: 
                print("La Ganancia Total de la linea", linea1, "fue de", gananciatotal1)
                print("La Ganancia Total de la linea", linea2, "fue de", gananciatotal2)
                print("La Ganancia Total de la linea", linea3, "fue de", gananciatotal3)
                print("La Ganancia Total de la linea", linea4, "fue de", gananciatotal4)
            elif x3 == 2:
                print("El costo total de la linea", linea1, "fue de", costo_total )
                print("El costo total de la linea", linea2, "fue de", costo_total2)
                print("El costo total de la linea", linea3, "fue de", costo_total3)
                print("El costo total de la linea", linea4, "fue de", costo_total4)
            elif x3 == 3: 
                print("La Ganancia Neta de la linea", linea1, "fue de", ganancianeta1)
                print("La Ganancia Neta de la linea", linea2, "fue de", ganancianeta2)
                print("La Ganancia Neta de la linea", linea3, "fue de", ganancianeta3)
                print("La Ganancia Neta de la linea", linea4, "fue de", ganancianeta4)
            elif x3 == 4: 
                print("El indice de eficiencia de la linea", linea1, "fue de", indice1)
                print("El indice de eficiencia de la linea", linea2, "fue de", indice2)
                print("El indice de eficiencia de la linea", linea3, "fue de", indice3)
                print("El indice de eficiencia de la linea", linea4, "fue de", indice4)

            elif x3 == 5: 
                if indice1 > indice2 and indice1 > indice3 and indice1 > indice4: 
                    print("La linea", linea1, "tuvo un mayor indice de eficiencia")

                elif indice2 > indice1 and indice2 > indice3 and indice2 > indice4:
                    print("La linea", linea2, "tuvo un mayor indice de eficiencia")

                elif indice3 > indice1 and indice3 > indice2 and indice3 > indice4:
                    print("La linea", linea3, "tuvo un mayor indice de eficiencia")

                elif indice4 > indice1 and indice4 > indice2 and indice4 > indice3: 
                    print("La linea", linea4, "tuvo un mayor indice de eficiencia")

            elif x3 == 6:
                opciones3 = False
                
            else: 
                print("ingrese una opcion valida")