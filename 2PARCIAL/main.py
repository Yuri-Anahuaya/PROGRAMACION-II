from persona import Persona
from linea import Linea
from mi_teleferico import MiTeleferico

# Crear teleférico
mt = MiTeleferico()

# Crear línea
linea_amarilla = Linea("Amarilla")
linea_amarilla.agregarCabina(1)
linea_amarilla.agregarCabina(2)

# Agregar línea al teleférico
mt.agregarLinea(linea_amarilla)

# Crear personas
p1 = Persona("Juan", 20, 70)
p2 = Persona("Luis", 30, 80)
p3 = Persona("Ana", 65, 65)

# Agregar personas
linea_amarilla.agregarPrimeraPersona(p1, 1)
linea_amarilla.cabinas[0].agregarPersona(p2)
linea_amarilla.cabinas[0].agregarPersona(p3)

# Verificar reglas
print("Reglas correctas:", linea_amarilla.verificarReglas())

# Ingreso total
print("Ingreso total:", linea_amarilla.ingresoTotal())

# Línea con más ingreso regular
mayor, ing = mt.lineaMayorIngresoRegular()
print("Línea con mayor ingreso regular:", mayor.color, "- Bs", ing)
