class Persona:
    def __init__(self):
        self.nombre = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = "" 

    def ingresar_datos(self):
        self.nombre = input("Ingrese sus nombres: ")
        self.apellidos = input("Ingrese sus apellidos: ")
        _apellido_casada = input("¿Tiene apellido de casada? (Sí/No): ")
        if _apellido_casada == "si":
            self.apellido_casada = input("Ingrese el apellido de casada: ")
        self.fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def obtener_nombre_completo(self):
        nombre_completo = self.nombre + " " + self.apellidos
        if self.apellido_casada:
            nombre_completo += " de " + self.apellido_casada
        return nombre_completo

x_persona = Persona()
x_persona.ingresar_datos()
print("Nombre Completo:", x_persona.obtener_nombre_completo())
print("Fecha de Nacimiento:", x_persona.obtener_fecha_nacimiento())





    

