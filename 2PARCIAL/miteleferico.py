from linea import Linea

class MiTeleferico:
    def __init__(self):
        self.lineas = []  # lista de Linea

    def agregarLinea(self, linea):
        self.lineas.append(linea)

    # d) mostrar línea con mayor ingreso SOLO con tarifa regular
    def lineaMayorIngresoRegular(self):
        mayor = None
        mayor_ingreso = 0

        for linea in self.lineas:
            ingreso = 0
            for cab in linea.cabinas:
                for p in cab.personasAbordo:
                    if 25 <= p.edad <= 60:
                        ingreso += 3
            if ingreso > mayor_ingreso:
                mayor_ingreso = ingreso
                mayor = linea

        return mayor, mayor_ingreso
