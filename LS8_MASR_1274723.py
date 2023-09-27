codigo = True 
while codigo: 
    print("1 factorial")
    print("2 secuencia de fibonacci")
    print("3 salir")
    x = int(input("ingrese la opcion que desea: "))

    if x == 1:
        a = int(input("ingrese el numero a operar= "))
        factorial = 1
        c = 1
        if a < 0:
            print("elija un numero positivo")
        elif a >= 0:
            for i in range(1, a+1):
                factorial = factorial * c
                c = c + 1
                print( a, "x", factorial, "=", factorial)

    elif x == 2:
        z = int(input("numero de posicion: "))
        for i in range(1,z):
          if z < 2:
                print(z)
        else:
            u = ((1+(5)**0.5)/2)
            j = ((u**z-(1-u)**z)/(5)**0.5)
            print("la posicion", z, "es",round(j))
    elif x>3: 
        print("elija una opcion valida")

    else:
        x==3 
        m = input("¿desde salir de las opciones? (si-no):")
        if m == "si":
                print("hasta luego")
                codigo=False
        else: 
                m=="no"
                codigo=True
            



