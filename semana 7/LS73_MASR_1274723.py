CODIGO = True
while CODIGO: 
    print("ejercicio 3 jerarquia de operaciones")
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("ingrese el tercer numero: "))

    print("1. a*b+c")
    print("2. a*(b+c)")
    print("3. a/b+c")
    print("4. 3a+2b/c**2")
    print("5. cuadratica")
    print("6. salir")

    opcion = input("elija la ecuacion que desea: ")

    if opcion=="1":
        operacion1= (a*b)+c
        print("resultado de: ", a, "*", b, "+", c, "=", operacion1)
    elif opcion=="2":
        operacion2= a *(b+c)
        print("resultado de: ", a, "*", "(", b, "+", c, ")", "=", operacion2)
    elif opcion=="3":
        operacion3= a/(b+c)
        print("resultado de: ", a, "/", "(", b, "+", c, ")", "=", operacion3)
    elif opcion=="4":
        operacion4= ((3*a)+(2*b))/c**2
        print("resultado de: ""(3 ", a, ")", "+", "(", "2 *", b, ")", "/", c,"* 2", "=", operacion4) 
    elif opcion=="5": 
        discriminante = (b ** 2) - (4 * a * c) 
        x1 = (-b+(discriminante)**0.5)/(2*a) 
        x2 = (-b-(discriminante)**0.5)/(2*a)
        if a==0: 
            print("a no puede ser 0") 
        elif discriminante <= 0:
            print("el discriminante no puede ser 0 o menor que 0")
        else:
            print("x1= ", x1)
            print("x2=", x2)
    elif opcion =="6":
        print("¡hasta luego!")
        CODIGO = False
    else: 
        print("Opción no válida. Por favor, elija una opción válida (1-6).")

    
        
