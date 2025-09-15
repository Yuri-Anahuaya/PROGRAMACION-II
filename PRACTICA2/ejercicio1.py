import math 
class AlgebraVectorial:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z



    def __add__(self, otro):
        return AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def __sub__(self, otro):
        return AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    def producto_vectorial(self, otro):
        cx = self.y * otro.z - self.z * otro.y
        cy = self.z * otro.x - self.x * otro.z
        cz = self.x * otro.y - self.y * otro.x
        return AlgebraVectorial(cx, cy, cz)

    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalizar(self):
        l = self.longitud()
        if l==0:
            raise ValueError("No se puede normalizar el vector nulo")
        return AlgebraVectorial(self.x / l, self.y / l, self.z / l)


    def es_perpendicular(self, otro, metodo=1):
        if metodo == 1:
            return math.isclose(self.producto_escalar(otro), 0.0)
        elif metodo == 2:
            return math.isclose((self + otro).longitud(), (self - otro).longitud())
        elif metodo == 3:
            return math.isclose((self + otro).longitud()**2, self.longitud()**2 + otro.longitud()**2)
        else:
            raise ValueError("Metodo no valido para verificar perpendicularidad")

    def es_paralelo(self, otro, metodo=1):
        """Verifica si dos vectores son paralelos"""
        if metodo == 1:
            # producto vectorial = 0
            return math.isclose(self.producto_vectorial(otro).longitud(), 0.0)
        elif metodo == 2:
            # comprobar si a = r*b
            try:
                r1 = self.x / otro.x if otro.x != 0 else None
                r2 = self.y / otro.y if otro.y != 0 else None
                r3 = self.z / otro.z if otro.z != 0 else None
                # Filtramos los None y verificamos si los cocientes son iguales
                ratios = [r for r in (r1, r2, r3) if r is not None]
                return all(math.isclose(r, ratios[0]) for r in ratios)
            except ZeroDivisionError:
                return False
        else:
            raise ValueError("Método no válido para verificar paralelismo")

    # ---------- Proyección y componente ----------
    def proyeccion_sobre(self, otro):
        """Proyección de self sobre otro"""
        escalar = self.producto_escalar(otro) / (otro.longitud()**2)
        return AlgebraVectorial(round(otro.x * escalar, 4),
                                round(otro.y * escalar, 4),
                                round(otro.z * escalar, 4))

    def componente_en(self, otro):
        """Componente de self en la dirección de otro"""
        return round(self.producto_escalar(otro) / otro.longitud(), 4)

    # ---------- Representación ----------
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"



# Vectores de prueba
a = AlgebraVectorial(2, 3, 1)
b = AlgebraVectorial(4, 6, 2)  # Este es paralelo a a (es 2*a)

c = AlgebraVectorial(1, 2, 3)
d = AlgebraVectorial(4, 0, -8)  # No paralelos, no perpendiculares

# Verificando a y b
print("Caso_Prueba: 1")
print("=======================")
print("Vector a:", a)
print("Vector b:", b)
print("¿a ⟂ b?", a.es_perpendicular(b))
print("¿a ∥ b?", a.es_paralelo(b))
print("Proyección de a sobre b:", a.proyeccion_sobre(b))
print("Componente de a en b:", a.componente_en(b))
print("_______________________")

# Verificando c y d
print("Caso_Prueba: 2")
print("=======================")
print("Vector c:", c)
print("Vector d:", d)
print("¿c ⟂ d?", c.es_perpendicular(d))
print("¿c ∥ d?", c.es_paralelo(d))
print("Proyección de c sobre d:", c.proyeccion_sobre(d))
print("Componente de c en d:", c.componente_en(d))

