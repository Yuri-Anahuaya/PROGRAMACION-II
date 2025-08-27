import math
class Estadistica:
    def __init__(self, datos):
        self.datos = datos

    def promedio(self):
        return sum(self.datos) / len(self.datos)

    def desviacion(self):
        prom = self.promedio()
        suma = sum((x - prom) ** 2 for x in self.datos)
        return math.sqrt(suma / (len(self.datos) - 1))


datos = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))
est = Estadistica(datos)
print(f"El promedio es {est.promedio():.2f}")
print(f"La desviación estándar es {est.desviacion():.5f}")
