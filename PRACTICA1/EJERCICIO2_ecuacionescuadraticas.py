import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c

    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return None
        return (-self.b + math.sqrt(disc)) / (2 * self.a)

    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return None
        return (-self.b - math.sqrt(disc)) / (2 * self.a)

a, b, c = map(float, input("Ingrese a b c: ").split())
eq = EcuacionCuadratica(a, b, c)
disc = eq.getDiscriminante()
if disc > 0:
    print("La ecuación tiene dos raíces:", eq.getRaiz1(), "y", eq.getRaiz2())
elif disc == 0:
    print("La ecuación tiene una raíz:", eq.getRaiz1())
else:
    print("La ecuación no tiene raíces reales")
