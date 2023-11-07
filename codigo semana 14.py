class Automovil:
    def __init__(self, modelo=0, precio=0.0, marca="", disponible=False, tipoCambioDolar=0.0, descuentoAplicado=0.0):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.disponible = disponible
        self.tipoCambioDolar = tipoCambioDolar
        self.descuentoAplicado = descuentoAplicado

    def DefinirModelo(self, Modelox):
        self.modelo = Modelox

    def DefinirPrecio(self, Preciox):
        self.precio = Preciox

    def DefinirMarca(self, Marcax):
        self.marca = Marcax

    def DefinirTipoCambio(self, TipoCambiox):
        self.tipoCambioDolar = TipoCambiox

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible"

    def MostrarInformacion(self):
        precio_dolares = self.precio / self.tipoCambioDolar
        disponibilidad = self.MostrarDisponibilidad()
        return ("Marca:", self.marca, "Modelo:", self.modelo, "Precio de venta:" "Q",self.precio, "Precio en dólares: $",precio_dolares, {disponibilidad})

    def AplicarDescuento(self, Descuentox):
        self.descuentoAplicado = Descuentox
        self.DefinirPrecio(self.precio * (1 - self.descuentoAplicado))

automovil = Automovil(modelo=2023, precio=25000.0, marca="Toyota", disponible=True, tipoCambioDolar=7.8, descuentoAplicado=0.1)
automovil.CambiarDisponibilidad()
automovil.AplicarDescuento(0.05)

print(automovil.MostrarInformacion())
