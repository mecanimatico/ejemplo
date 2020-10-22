class Buseta:
    def __init__(self, cantidad_puestos):
        self.listado_puestos = [None]*cantidad_puestos

    def vender_pasaje(self, puesto, persona):
        lugar = self.listado_puestos[int(puesto)-1]
        if (lugar):
            print("Lugar ocupado")
        else:
            self.listado_puestos[int(puesto)-1] = persona
            return "Puesto asignado a: " + persona.nombre_completo()

    def mostrar_sillas_disponibles(self):
        sillas_disponibles = []
        for indice, lugar in enumerate(self.listado_puestos, start=0):
            if lugar == None:
                sillas_disponibles.append(indice + 1)
        return sillas_disponibles 
    
    def puestos_libres_ventana(self):
        sillas_ventana = []
        sillas_disponibles = self.mostrar_sillas_disponibles()
        for silla in sillas_disponibles:
            if silla % 2 == 0:
                sillas_ventana.append(silla)
        return sillas_ventana

    def puestos_libres_pasillo(self):
        sillas_pasillo = []
        sillas_disponibles = self.mostrar_sillas_disponibles()
        for silla in sillas_disponibles:
            if silla % 2 != 0:
                sillas_pasillo.append(silla)
        return sillas_pasillo

    def listar_pasajeros(self):
        lista = []
        for pasajero in self.listado_puestos:
            if pasajero != None:
                lista.append(pasajero.nombre_completo())
        return lista


       
  