print("ejercicio 3 jerarquia de operaciones")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("ingrese el tercer numero: "))

print("1. a*b+c")
print("2. a*(b+c)")
print("3. a/b+c")
print("4. 3a+2b/c**2")
print("5. adios")

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
else :
    opcion=="4"
    operacion4= ((3*a)+(2*b))/c**2
    print("resultado de: ""(3 *", a, ")", "+", "(", "2 *", b, ")", "/", c,"** 2", "=", operacion4)

