# juego.py

class Juego:
    def __init__(self, numeroDeVidas: int):
        self.vidasIniciales = numeroDeVidas
        self.numeroDeVidas = numeroDeVidas
        self.record = 0  # El mejor resultado de vidas restantes al ganar

    def reiniciaPartida(self):
        """Reinicia las vidas actuales a las vidas iniciales."""
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        """Actualiza el record si las vidas actuales superan al record previo."""
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
            print(f"🎖️ ¡Nuevo record! Vidas restantes: {self.record}")

    def quitaVida(self) -> bool:
        """
        Quita una vida y retorna True si aún quedan vidas.
        Retorna False si se acabaron.
        """
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

    def getVidasActuales(self) -> int:
        return self.numeroDeVidas
