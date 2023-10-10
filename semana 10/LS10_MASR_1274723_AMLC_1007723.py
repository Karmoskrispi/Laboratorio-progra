def DecimalAHexadecimal(): 
    decimal = int(input("Introduzca un numero: ")) 
    hexadecimal = "" 
    while decimal != 0: 
        a = CambiarDigitos(decimal % 16)
        hexadecimal = str(a) + hexadecimal
        decimal = int(decimal / 16)
    print("Resultado: " + hexadecimal) 

def CambiarDigitos(digitos): 
    decimales =     [10 , 11 , 12 , 13 , 14 , 15 ]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for c in range(7):
        if digitos == decimales[c - 1]:
            digitos = hexadecimal[c - 1]
    return digitos

DecimalAHexadecimal()