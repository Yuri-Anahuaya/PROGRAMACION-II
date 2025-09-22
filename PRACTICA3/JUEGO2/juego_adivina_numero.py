# juego_adivina_numero.py
from juego import Juego
import random

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas: int):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = None

    def validaNumero(self, numero: int):
        if 0 <= numero <= 10:
            return True, None
        return False, "Número fuera de rango. Debe estar entre 0 y 10."

    def juega(self, titulo: str = None):
        self.reiniciaPartida()

        # ✅ Si no se estableció número secreto, generarlo automáticamente
        if self.numeroAAdivinar is None:
            self.numeroAAdivinar = random.randint(0, 10)

        # Mostrar título personalizado o genérico
        if titulo:
            print(f"\n=== {titulo} ===")
        else:
            print("\n=== Juego: Adivina el número (0-10) ===")

        print(f"Tienes {self.vidasIniciales} vidas.")

        # Bucle principal de juego
        while self.getVidasActuales() > 0:
            intento = int(input("Ingresa tu número: "))

            valido, msg = self.validaNumero(intento)
            if not valido:
                print(f"❌ {msg}")
                continue

            if intento == self.numeroAAdivinar:
                print("✅ ¡Acertaste!")
                self.actualizaRecord()
                self.numeroAAdivinar = None  # Reiniciar para la próxima partida
                return

            # intento válido pero incorrecto -> quitar vida
            quedan = self.quitaVida()
            if quedan:
                if intento < self.numeroAAdivinar:
                    print(f"El número a adivinar es MAYOR. Vidas restantes: {self.getVidasActuales()}")
                else:
                    print(f"El número a adivinar es MENOR. Vidas restantes: {self.getVidasActuales()}")
            else:
                print(f"💀 Te quedaste sin vidas. El número era: {self.numeroAAdivinar}")
                self.numeroAAdivinar = None  # Reiniciar para la próxima partida
                return
