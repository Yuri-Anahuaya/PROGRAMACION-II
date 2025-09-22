# juego.py
class Juego:
    def __init__(self, numeroDeVidas: int):
        self.vidasIniciales = numeroDeVidas
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print(f"🎖️ ¡Nuevo record! Vidas restantes: {self.record}")

    def quitaVida(self) -> bool:
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

    def getVidasActuales(self) -> int:
        return self.numeroDeVidas
