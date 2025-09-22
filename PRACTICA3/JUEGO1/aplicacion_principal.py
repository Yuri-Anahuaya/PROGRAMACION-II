# aplicacion.py
from juego_adivina_numero import JuegoAdivinaNumero

class Aplicacion:
    @staticmethod
    def main():
        # Juego con 3 vidas
        juego = JuegoAdivinaNumero(3)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()

