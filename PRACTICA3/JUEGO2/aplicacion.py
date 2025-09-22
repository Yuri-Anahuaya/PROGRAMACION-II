# aplicacion.py
from juego_adivina_numero import JuegoAdivinaNumero
from juego_adivina_par import JuegoAdivinaPar
from juego_adivina_impar import JuegoAdivinaImpar

def main():
    print("Bienvenido a los Juegos de Adivinanza 🎲")

    juegoNormal = JuegoAdivinaNumero(3)
    juegoPar = JuegoAdivinaPar(3)
    juegoImpar = JuegoAdivinaImpar(3)

    juegoNormal.juega()
    juegoPar.juega()
    juegoImpar.juega()

if __name__ == "__main__":
    main()
