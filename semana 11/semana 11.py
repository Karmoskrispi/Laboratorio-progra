cadena = input("ingrese una cadena de caracteres: ")
uno = 0 
cero = 0 
otros = 0 

for x in cadena: 
    if x == "1": 
        uno += 1
    elif x == "0": 
        cero += 1
    else: 
        otros += 1
print("cantidad de unos: ", uno) 
print("cantidad de ceros: ", cero)
print("cantridad de caracteres diferentes: ", otros) 