# juego_adivina_numero.py
from juego import Juego
import random

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas: int):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        """Lógica principal para jugar a adivinar el número."""
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("=== Juego: Adivina el número (0-10) ===")
        print(f"Tienes {self.vidasIniciales} vidas para adivinar.\n")

        while self.getVidasActuales() > 0:
            numeroUsuario = int(input("Ingresa un número entre 0 y 10: "))

            if numeroUsuario == self.numeroAAdivinar:
                print("🎉 ¡Acertaste!")
                self.actualizaRecord()
                return  # Termina el juego al acertar

            # Si falló, quita vida
            if self.quitaVida():
                if numeroUsuario < self.numeroAAdivinar:
                    print("El número secreto es MAYOR.")
                else:
                    print("El número secreto es MENOR.")
                print(f"Vidas restantes: {self.getVidasActuales()}\n")
            else:
                print("💀 Te quedaste sin vidas.")
                print(f"El número secreto era: {self.numeroAAdivinar}")
                return
