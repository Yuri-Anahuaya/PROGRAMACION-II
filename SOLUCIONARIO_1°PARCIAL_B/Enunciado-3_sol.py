class Profesional:
    def __init__(self, nombre, edad, años):
        self.nombre = nombre
        self.edad = edad
        self.años = años

    def mostrar(self):
        print(self.nombre, "-", self.edad, "años,", self.años, "años de estudio")

    def comparar(self, otro, atributo):
        if atributo == "edad":
            if self.edad > otro.edad:
                print(self.nombre, "es mayor que", otro.nombre)
            elif self.edad < otro.edad:
                print(otro.nombre, "es mayor que", self.nombre)
            else:
                print("Tienen la misma edad")
        elif atributo == "años":
            if self.años > otro.años:
                print(self.nombre, "tiene más años de estudio que", otro.nombre)
            elif self.años < otro.años:
                print(otro.nombre, "tiene más años de estudio que", self.nombre)
            else:
                print("Tienen los mismos años de estudio")

def promedio_estudio(lista):
    suma = 0
    for p in lista:
        suma = suma + p.años
    prom = suma / len(lista)
    return prom


class Nutricionista(Profesional):
    def __init__(self, nombre, edad, años, especialidad, pacientes, dieta):
        super().__init__(nombre, edad, años)
        self.especialidad = especialidad
        self.pacientes = pacientes
        self.dieta = dieta

    def mostrar(self):
        print("Nutricionista:", self.nombre, "-", self.especialidad,
              "-", self.pacientes, "pacientes - dieta:", self.dieta)


class Abogado(Profesional):
    def __init__(self, nombre, edad, años, especialidad, bufete, casos):
        super().__init__(nombre, edad, años)
        self.especialidad = especialidad
        self.bufete = bufete
        self.casos = casos

    def mostrar(self):
        print("Abogado:", self.nombre, "-", self.especialidad,
              "-", self.bufete, "-", self.casos, "casos resueltos")


class Informatico(Profesional):
    def __init__(self, nombre, edad, años, lenguaje, experiencia, proyectos):
        super().__init__(nombre, edad, años)
        self.lenguaje = lenguaje
        self.experiencia = experiencia
        self.proyectos = proyectos

    def mostrar(self):
        print("Informático:", self.nombre, "-", self.lenguaje,
              "-", self.experiencia, "años exp. -", self.proyectos, "proyectos")


# Crear objetos
n1 = Nutricionista("María Lopez", 29, 5, "Deportiva", 30, "Proteica")
a1 = Abogado("Carlos Pérez", 40, 6, "Civil", "Bufete Legal SRL", 120)
a2 = Abogado("Ana Torres", 35, 7, "Penal", "Justicia Total", 90)
i1 = Informatico("Luis Romero", 27, 4, "Python", 3, 15)
i2 = Informatico("Sofía Gutiérrez", 30, 5, "Java", 5, 22)

# lista general
lista = [n1, a1, a2, i1, i2]

print("\n=== DATOS DE PROFESIONALES ===")
for p in lista:
    p.mostrar()

# comparar atributos
print("\n=== COMPARACIONES ===")
a1.comparar(a2, "edad")
i1.comparar(i2, "años")

# promedio
prom = promedio_estudio(lista)
print("\nPromedio de años de estudio:", prom)
