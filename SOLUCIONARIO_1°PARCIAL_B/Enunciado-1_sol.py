# Sistema de Parqueo Tarifado en La Paz

class ParqueoTarifado:
    def __init__(self, codigo, empresa, tarifa):
        self.codigo = codigo
        self.empresa = empresa
        self.tarifa = tarifa
        self.vehiculos = []  # lista de vehículos registrados

    def habilitarZona(self):
        print("Zona de parqueo habilitada en la calle:", self.codigo)

    def verificarPago(self, placa):
        for v in self.vehiculos:
            if v.placa == placa:
                print("El vehículo", placa, "tiene pago registrado.")
                return
        print("El vehículo", placa, "no tiene pago registrado.")

    def aplicarMulta(self, placa):
        print("Vehículo", placa, "multado por falta de pago.")

    def agregarVehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print("Vehículo agregado al parqueo:", vehiculo.placa)


class Vehiculo:
    def __init__(self, placa, tipo, propietario):
        self.placa = placa
        self.tipo = tipo
        self.propietario = propietario

    def ingresar(self):
        print("El vehículo", self.placa, "ingresó al parqueo.")

    def salir(self):
        print("El vehículo", self.placa, "salió del parqueo.")

    def calcularDuracion(self, h1, h2):
        duracion = h2 - h1
        print("El vehículo", self.placa, "estuvo", duracion, "horas.")
        return duracion


class PagoPorTiempo:
    def __init__(self, horaIngreso, horaSalida, monto):
        self.horaIngreso = horaIngreso
        self.horaSalida = horaSalida
        self.monto = monto

    def calcularMonto(self, tarifa):
        horas = self.horaSalida - self.horaIngreso
        self.monto = horas * tarifa
        print("Monto calculado:", self.monto, "Bs")
        return self.monto

    def generarQR(self):
        print("Código QR generado para el pago:", self.monto, "Bs")

    def confirmarPago(self):
        print("Pago confirmado con éxito.")


class RegistroMunicipal:
    def __init__(self, nombre, zona, nroEmpresas):
        self.nombre = nombre
        self.zona = zona
        self.nroEmpresas = nroEmpresas

    def registrarEmpresa(self, empresa):
        print("Empresa registrada:", empresa)

    def emitirPermiso(self):
        print("Permiso emitido para operar en la zona:", self.zona)

    def controlarRecaudacion(self):
        print("Controlando recaudación en la zona:", self.zona)


# ===============================
# PROGRAMA PRINCIPAL DE PRUEBA
# ===============================

print("=== SISTEMA DE PARQUEO TARIFADO ===")

# Crear registro municipal
r = RegistroMunicipal("Alcaldía de La Paz", "Centro", 4)
r.registrarEmpresa("ParqueoParaTodos S.A.")
r.emitirPermiso()

# Crear parqueo
p = ParqueoTarifado("Calle Comercio", "ParqueoParaTodos", 5)
p.habilitarZona()

# Crear vehículos
v1 = Vehiculo("3456PIB", "Automóvil", "Marcia Lira")
v2 = Vehiculo("1245AXD", "Motocicleta", "Luis Jairo")

# Ingresar vehículos
v1.ingresar()
v2.ingresar()

# Agregarlos al parqueo
p.agregarVehiculo(v1)
p.agregarVehiculo(v2)

# Verificar pago y aplicar multa
p.verificarPago("3456PIB")
p.aplicarMulta("1245AXD")

# Crear pago
pago1 = PagoPorTiempo(9, 12, 0)
monto1 = pago1.calcularMonto(p.tarifa)
pago1.generarQR()
pago1.confirmarPago()

# Salida de vehículo
v1.calcularDuracion(9, 12)
v1.salir()
