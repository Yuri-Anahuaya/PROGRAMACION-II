import math 
class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z



    def __add__(self, otro):
        return Vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def __sub__(self, otro):
        return Vector3D(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __mul__(self, escalar):
        return Vector3D(self.x * escalar, self.y * escalar, self.z * escalar)

    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalizar(self):
        l = self.longitud()
        if l==0:
            raise ValueError("No se puede normalizar el vector nulo")
        return Vector3D(round(self.x / l, 4),
                        round(self.y / l, 4),
                        round(self.z / l, 4))

    def producto_escalar(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def producto_vectorial(self, otro):
        cx = self.y * otro.z - self.z * otro.y
        cy = self.z * otro.x - self.x * otro.z
        cz = self.x * otro.y - self.y * otro.x
        return Vector3D(cx, cy, cz)

    
    
    

    def es_perpendicular(self, otro, metodo=1):
        if metodo == 1:
            return math.isclose(self.producto_escalar(otro), 0.0)
        elif metodo == 2:
            return math.isclose((self + otro).longitud(), (self - otro).longitud())
        elif metodo == 3:
            return math.isclose((self + otro).longitud()**2, self.longitud()**2 + otro.longitud()**2)
        else:
            raise ValueError("Metodo no valido")


    def es_paralelo(self, otro, metodo=1):
        """Verifica si dos vectores son paralelos"""
        if metodo == 1:
            # producto vectorial = 0
            return math.isclose(self.producto_vectorial(otro).longitud(), 0.0)
        elif metodo == 2:
            ratios = []
            for s, o in zip ((self.x, self.y, self.z), (otro.x, otro.y, otro.z)):
                if o != 0:
                    ratios.append(s/o)
            return all(math.isclose(r, ratios[0]) for r in ratios)
        else:
            raise ValueError("Metodo no valido")



            
    # ---------- Proyección y componente ----------
    def proyeccion_sobre(self, otro):
        """Proyección de self sobre otro"""
        escalar = self.producto_escalar(otro) / (otro.longitud()**2)
        return Vector3D(round(otro.x * escalar, 4),
                                round(otro.y * escalar, 4),
                                round(otro.z * escalar, 4))

    def componente_en(self, otro):
        """Componente de self en la dirección de otro"""
        return round(self.producto_escalar(otro) / otro.longitud(), 4)

    # ---------- Representación ----------
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"



"""
a = Vector3D(1, 0, 0)
b = Vector3D(0, 1, 0)

print("Vector a:", a)
print("Vector b:", b)
print("Suma a + b:", a + b)
print("Resta a - b:", a - b)
print("Multiplicacion de a por escalar 3:", a * r)
print("Longitud de a:", round(a.longitud(), 2))
print("Vector unitario de a:", a.normalizar())
print("Producto escalar a·b:", a.producto_escalar(b))
print("Producto Vectorial a×b:", a.producto_vectorial(b))
print("¿a ⟂ b?", a.es_perpendicular(b))
print("¿a ∥ b?", a.es_paralelo(b))
print("Proyección de a sobre b:", a.proyeccion_sobre(b))
print("Componente de a en b:", a.componente_en(b))
print()
"""

# Vectores de prueba
a = Vector3D(2, 3, 1)
b = Vector3D(4, 6, 2)  # Este es paralelo a a (es 2*a)

c = Vector3D(1, 2, 3)
d = Vector3D(4, 0, -8)  # No paralelos, no perpendiculares

r=3
# Verificando a y b
print("Caso_Prueba: 1")
print("=======================")
print("Vector a:", a)
print("Vector b:", b)
print("Suma a + b:", a + b)
print("Resta a - b:", a - b)
print("Multiplicacion de a por escalar 3:", a * r)
print("Longitud de a:", round(a.longitud(), 2))
print("Vector unitario de a:", a.normalizar())
print("Producto escalar a·b:", a.producto_escalar(b))
print("Producto Vectorial a×b:", a.producto_vectorial(b))
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
print("Suma c + d:", c + d)
print("Resta c - d:", c - d)
print("Multiplicacion de a por escalar 3:", c * r)
print("Longitud de c:", round(c.longitud(), 2))
print("Vector unitario de c:", c.normalizar())
print("Producto escalar c·d:", c.producto_escalar(d))
print("Producto Vectorial c×d:", c.producto_vectorial(d))
print("¿c ⟂ d?", c.es_perpendicular(d))
print("¿c ∥ d?", c.es_paralelo(d))
print("Proyección de c sobre d:", c.proyeccion_sobre(d))
print("Componente de c en d:", c.componente_en(d))
