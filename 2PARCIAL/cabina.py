class Cabina:
    def __init__(self, nroCabina):
        self.nroCabina = nroCabina
        self.personasAbordo = []   # lista de objetos Persona

    def agregarPersona(self, persona):
        # Máximo 10 personas
        if len(self.personasAbordo) >= 10:
            print("❌ No se puede agregar más personas (máximo 10).")
            return False

        # Peso máximo de 850 kg por cabina
        peso_total = sum(p.peso for p in self.personasAbordo)
        if peso_total + persona.peso > 850:
            print("❌ Peso excedido, no se puede agregar a", persona.nombre)
            return False

        self.personasAbordo.append(persona)
        return True
