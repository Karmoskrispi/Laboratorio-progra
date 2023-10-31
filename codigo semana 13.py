class circulo: 
    def __init__(self, radio):
        self.radio= radio
    def obtener_perimetro(self):
        return 3.14*2* self.radio
    def obtener_area(self):
        return 3.14 * self.radio**2
    def obtener_volumen(self):
        return 4*3.14*self.radio/3
    
circulo1 = circulo(4) 
print(circulo1.obtener_perimetro())
print(circulo1.obtener_area())
print(circulo1.obtener_volumen())


