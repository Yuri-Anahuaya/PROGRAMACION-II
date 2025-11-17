from cabina import Cabina

class Linea:
    def __init__(self, color):
        self.color = color
        self.cabinas = []  # lista de objetos Cabina

    def agregarCabina(self, nroCab):
        cab = Cabina(nroCab)
        self.cabinas.append(cab)

    # a) agregar la primera persona a la cabina nro X
    def agregarPrimeraPersona(self, persona, nroCabina):
        for cab in self.cabinas:
            if cab.nroCabina == nroCabina:
                if len(cab.personasAbordo) == 0:
                    return cab.agregarPersona(persona)
                else:
                    print("❌ La cabina ya tiene personas, no es la primera.")
                    return False
        print("❌ No existe esa cabina.")
        return False

    # b) verificar que TODAS las cabinas cumplan las reglas
    def verificarReglas(self):
        for cab in self.cabinas:
            if len(cab.personasAbordo) > 10:
                return False
            if sum(p.peso for p in cab.personasAbordo) > 850:
                return False
        return True

    # c) ingreso total
    def ingresoTotal(self):
        total = 0
        for cab in self.cabinas:
            for p in cab.personasAbordo:
                if p.edad < 25 or p.edad > 60:
                    total += 1.5   # tarifa preferencial
                else:
                    total += 3     # tarifa regular
        return total
