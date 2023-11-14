class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.casillas = [['O' for _ in range(tamaño)] for _ in range(tamaño)]
        self.filas = "ABCDEFGHIJ"
        self.columnas = [str(i) for i in range(1, 11)]

    def mostrar(self):
        # Mostrar etiquetas de las columnas
        print("   " + " ".join(self.columnas))
        for i in range(len(self.casillas)):
            # Mostrar etiquetas de las filas
            mostrar_fila = [self.filas[i]] + self.casillas[i]
            print(" ".join(mostrar_fila))

class Barco:
    def __init__(self, tamaño, orientacion):
        self.tamaño = tamaño
        self.orientacion = orientacion
        self.casillas = []

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero(10)
        self.barcos = {'pequeños': 3, 'grandes': 2}

    def colocar_barcos(self):
        print(self.nombre, "coloca tus barcos en el tablero (deben ser 3 pequeños y 2 grandes):")
        for _ in range(self.barcos['pequeños']):
            self.colocar_barco(3)
        for _ in range(self.barcos['grandes']):
            self.colocar_barco(5)

    def colocar_barco(self, tamaño):
        print("Coloca un barco de tamaño", tamaño, "en el tablero:")
        fila, columna = self.adivinar_coordenadas()
        orientacion = input("Elige la orientación (H para horizontal, V para vertical): ").upper()

        while not self.validar_colocacion(fila, columna, tamaño, orientacion):
            print("Colocación no válida. Intenta de nuevo.")
            fila, columna = self.adivinar_coordenadas()
            orientacion = input("Elige la orientación (H para horizontal, V para vertical): ").upper()

        nuevo_barco = Barco(tamaño, orientacion)
        for i in range(tamaño):
            if orientacion == "H":
                self.tablero.casillas[fila][columna + i] = 'B'
                nuevo_barco.casillas.append((fila, columna + i))
            elif orientacion == "V":
                self.tablero.casillas[fila + i][columna] = 'B'
                nuevo_barco.casillas.append((fila + i, columna))

    def validar_colocacion(self, fila, columna, tamaño, orientacion):
        if orientacion == "H":
            if columna + tamaño > self.tablero.tamaño:
                return False
            for i in range(tamaño):
                if self.tablero.casillas[fila][columna + i] == 'B':
                    return False
        elif orientacion == "V":
            if fila + tamaño > self.tablero.tamaño:
                return False
            for i in range(tamaño):
                if self.tablero.casillas[fila + i][columna] == 'B':
                    return False
        return True

    def adivinar_coordenadas(self):
        while True:
            coordenadas = input("Ingresa la coordenada de inicio (por ejemplo, A2): ").upper()

            if len(coordenadas) == 2 and coordenadas[0] in self.tablero.filas:
                fila = self.tablero.filas.find(coordenadas[0])
                
                # Verificar si la parte numérica es un dígito
                columna_str = coordenadas[1]
                if not columna_str.isdigit():
                    print("Número de columna no válido. Por favor, ingresa valores válidos.")
                    continue
                
                columna = int(columna_str) - 1

                if 0 <= columna < self.tablero.tamaño:
                    return fila, columna
                else:
                    print("Número de columna no válido. Por favor, ingresa valores válidos.")
            else:
                print("Coordenadas no válidas. Por favor, ingresa valores válidos.")

def disparar(jugador, oponente):
    print(f"\nTurno de", jugador.nombre, "para disparar:")
    oponente.tablero.mostrar()

    fila, columna = jugador.adivinar_coordenadas()

    if oponente.tablero.casillas[fila][columna] == 'B':
        print("¡Impacto! Golpeaste un barco.")
        oponente.tablero.casillas[fila][columna] = 'X'
    else:
        print("Agua. No golpeaste ningún barco.")
        oponente.tablero.casillas[fila][columna] = '-'

    if not any('B' in fila for fila in oponente.tablero.casillas):
        print("¡", jugador.nombre, "ha hundido todos los barcos de", oponente.nombre, "!")


def jugar():
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")

    print("¡Bienvenido a Batalla Naval!")

    jugador1.colocar_barcos()
    jugador2.colocar_barcos()

    turno = jugador1

    while True:
        disparar(turno, jugador2)
        if not any('B' in fila for fila in jugador2.tablero.casillas):
            print("¡", jugador1.nombre, "ha ganado!")
            break

        input("Presiona Enter para continuar...")
        turno = jugador1 if turno == jugador2 else jugador2


if __name__ == "__main__":
    jugar()

