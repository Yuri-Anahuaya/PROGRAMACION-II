# juego_adivina_impar.py
import random
from juego_adivina_numero import JuegoAdivinaNumero

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas: int):
        super().__init__(numeroDeVidas)

    def validaNumero(self, numero: int):
        if not (0 <= numero <= 10):
            return False, "Número fuera de rango. Debe estar entre 0 y 10."
        if numero % 2 == 0:
            return False, "El número debe ser IMPAR."
        return True, None

    def juega(self):
        # Generar número secreto que sea IMPAR
        impares = [n for n in range(0, 11) if n % 2 != 0]
        self.numeroAAdivinar = random.choice(impares)

        super().juega(titulo="Juego: Adivina el número IMPAR (0-10)")
