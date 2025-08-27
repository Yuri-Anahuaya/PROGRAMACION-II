class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.a, self.b, self.c, self.d, self.e, self.f = a, b, c, d, e, f

    def tieneSolucion(self):
        return (self.a * self.d - self.b * self.c) != 0

    def getX(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)

    def getY(self):
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)


a, b, c, d, e, f = map(float, input("Ingrese a b c d e f: ").split())
eq = EcuacionLineal(a, b, c, d, e, f)
if eq.tieneSolucion():
    print("x =", eq.getX())
    print("y =", eq.getY())
else:
    print("La ecuación no tiene solución")
