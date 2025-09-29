from abc import ABC, abstractmethod
import random

# --------------------------
# Interfaz Coloreado
# --------------------------
class Coloreado:
    def comoColorear(self):
        pass


# --------------------------
# Clase abstracta Figura
# --------------------------
class Figura(ABC):
    def __init__(self, color):
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return "Figura de color: " + self.color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


# --------------------------
# Clase Cuadrado
# --------------------------
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados."

    def __str__(self):
        return ("Cuadrado de color " + self.color +
                ", lado: " + str(self.lado) +
                ", área: " + str(round(self.area(), 2)) +
                ", perímetro: " + str(round(self.perimetro(), 2)))


# --------------------------
# Clase Circulo
# --------------------------
class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.1416 * self.radio

    def __str__(self):
        return ("Círculo de color " + self.color +
                ", radio: " + str(self.radio) +
                ", área: " + str(round(self.area(), 2)) +
                ", perímetro: " + str(round(self.perimetro(), 2)))


# --------------------------
# Programa principal
# --------------------------
def main():
    figuras = []

    # Generamos 5 figuras al azar
    for i in range(5):
        tipo = random.randint(1, 2)  # 1=Cuadrado, 2=Círculo
        color = random.choice(["Rojo", "Azul", "Verde", "Amarillo"])

        if tipo == 1:
            lado = random.randint(1, 10)
            figuras.append(Cuadrado(lado, color))
        else:
            radio = random.randint(1, 10)
            figuras.append(Circulo(radio, color))

    # Mostrar información de cada figura
    print("\n--- Lista de Figuras ---")
    for f in figuras:
        print(f)
        if isinstance(f, Coloreado):
            print("Método Coloreado:", f.comoColorear())
        print("--------------------")


if __name__ == "__main__":
    main()
