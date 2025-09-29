from abc import ABC, abstractmethod

# Clase abstracta
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def CalcularSalarioMensual(self):
        pass

    def __str__(self):
        return "Empleado: " + self.nombre


# Clase EmpleadoTiempoCompleto
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salarioAnual):
        super().__init__(nombre)
        self.salarioAnual = salarioAnual

    def CalcularSalarioMensual(self):
        return self.salarioAnual / 12

    def __str__(self):
        return "Empleado Tiempo Completo: " + self.nombre + \
               ", Salario Anual: " + str(self.salarioAnual) + \
               ", Salario Mensual: " + str(round(self.CalcularSalarioMensual(), 2))


# Clase EmpleadoTiempoHorario
class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre, horasTrabajadas, tarifaPorHora):
        super().__init__(nombre)
        # Restricción realista
        if horasTrabajadas < 0 or horasTrabajadas > 744:
            print("Error: Las horas trabajadas deben estar entre 0 y 744.")
            horasTrabajadas = 0
        self.horasTrabajadas = horasTrabajadas
        self.tarifaPorHora = tarifaPorHora

    def CalcularSalarioMensual(self):
        return self.horasTrabajadas * self.tarifaPorHora

    def __str__(self):
        return "Empleado Tiempo Horario: " + self.nombre + \
               ", Horas: " + str(self.horasTrabajadas) + \
               ", Tarifa: " + str(self.tarifaPorHora) + \
               ", Salario Mensual: " + str(round(self.CalcularSalarioMensual(), 2))


# Programa principal
def main():
    empleados = []

    # Ingreso de 3 empleados a tiempo completo
    for i in range(3):
        nombre = input("Ingrese el nombre del empleado tiempo completo " + str(i+1) + ": ")
        salarioAnual = float(input("Ingrese el salario anual: "))
        emp = EmpleadoTiempoCompleto(nombre, salarioAnual)
        empleados.append(emp)

    # Ingreso de 2 empleados a tiempo horario
    for i in range(2):
        nombre = input("Ingrese el nombre del empleado tiempo horario " + str(i+1) + ": ")
        horas = float(input("Ingrese las horas trabajadas: "))
        tarifa = float(input("Ingrese la tarifa por hora: "))
        emp = EmpleadoTiempoHorario(nombre, horas, tarifa)
        empleados.append(emp)

    # Mostrar resultados
    print("\n--- Lista de Empleados ---")
    for e in empleados:
        print(e)


if __name__ == "__main__":
    main()
