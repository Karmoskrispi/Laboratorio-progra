while True: 
    print("Ejercicio 1: Operaciones Aritméticas")
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Exponenciación")
    print("7. Cociente")
    print("8. Salir")

    opcion = input("Elija una opción (1-8): ")

    if opcion == '1':
        resultado = x + y
        print(x, "+", y,  "=", resultado)
    elif opcion == '2':
        resultado = x - y
        print(x, "-", y,  "=", resultado)
    elif opcion == '3':
        resultado = x * y
        print(x, "*", y,  "=", resultado)
    elif opcion == '4':
        if y == 0:
            print("No se puede dividir por cero.")
        else:
            resultado = x / y
            print(x, "/", y,  "=", resultado)
    elif opcion == '5':
        resultado = x % y
        print(x, "%", y,  "=", resultado)
    elif opcion == '6':
        resultado = x ** y
        print(x, "**", y,  "=", resultado)
    elif opcion == '7':
        resultado = x // y
        print(x, "//", y,  "=", resultado)
    elif opcion == '8':
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, elija una opción válida (1-8).")
