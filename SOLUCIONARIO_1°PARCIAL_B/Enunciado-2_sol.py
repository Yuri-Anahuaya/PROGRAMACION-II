class Parqueo:
    def __init__(self, tarifa):
        self.nv = 0
        self.tarifa = tarifa
        self.vehiculos = []   # lista con [placa, conductor]
        self.tiempos = []     # lista con [hora_ingreso, hora_salida]

    # operador + para agregar un vehículo
    def __add__(self, dato):
        placa, conductor, h1, h2 = dato
        self.vehiculos.append([placa, conductor])
        self.tiempos.append([h1, h2])
        self.nv = self.nv + 1
        print("Vehículo agregado:", placa, "de", conductor)
        return self

    # buscar conductor por placa
    def buscarConductor(self, placa):
        for i in range(self.nv):
            if self.vehiculos[i][0] == placa:
                return self.vehiculos[i][1]
        return "No encontrado"

    # contar vehículos por horas de parqueo
    def contarPorHoras(self, horas):
        c = 0
        for i in range(self.nv):
            if self.tiempos[i][1] - self.tiempos[i][0] == horas:
                c = c + 1
        return c

    # mostrar datos del parqueo
    def mostrar(self):
        print("\nLISTA DE VEHÍCULOS:")
        for i in range(self.nv):
            print(self.vehiculos[i][0], "-", self.vehiculos[i][1],
                  "Ingreso:", self.tiempos[i][0],
                  "Salida:", self.tiempos[i][1])


# Programa principal
p = Parqueo(3)

# agregar los datos del enunciado
p + ("1245axd", "Luis Jairo", 2, 5)
p + ("3456pib", "Marcia Lira", 9, 12)
p + ("2576jux", "Pablo Rubio", 10, 12)
p + ("3221lip", "Rosa Jux", 10, 13)
p + ("3465kik", "Saul Lopez", 10, 11)

p.mostrar()

# buscar conductor
placa = "3456pib"
print("\nConductor del vehículo", placa, "es:", p.buscarConductor(placa))

# contar vehículos por duración
m = 3
print("Vehículos que estuvieron", m, "horas:", p.contarPorHoras(m))
