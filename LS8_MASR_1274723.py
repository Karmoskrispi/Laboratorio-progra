codigo = True 

while codigo: 
    print("1 factorial")
    print("2 secuencia de fibonacci")
    print("3 salir")
    x = int(input("ingrese la opcion que desea: "))

    if x == 1:
        a = int(input("ingrese el numero a operar= "))

    if a >= 1: 
        i = 1
        for a in range(1,i+1):
            resultado = (a*(a-1)) 
            a1 = i * resultado 
            print("el factorial es= ", a1)
            



