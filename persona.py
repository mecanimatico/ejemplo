class Persona:
    def __init__(self, nombre, apellido, cedula, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        
    def nombre_completo(self):
        return self.nombre + " " + self.apellido

