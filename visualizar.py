import cherrypy 
from buseta import Buseta
from persona import Persona
class Comercializar(object):
    def __init__(self):
        self.transporte = Buseta(40)
            
    @cherrypy.expose
    def index(self):
        return open("views/index.html")

    @cherrypy.expose
    def comprar_pasaje(self):
        return open("views/taquilla.html")
    
    @cherrypy.expose
    def tiquetear_pasaje(self,puesto, nombre, apellido, cedula, telefono):
        turista = Persona(nombre, apellido, cedula, telefono)
        self.transporte.vender_pasaje(puesto,turista)
        return "Pasaje asignado"
    
    @cherrypy.expose
    def mostrar_disponibles(self):
        return open("views/puestos_disponibles.html")

    @cherrypy.expose
    def mostrar(self):
        lista = self.transporte.mostrar_sillas_disponibles()
        return str(lista)

    @cherrypy.expose
    def puestos_ventana(self):
        return open ("views/puestos_disponibles_ventana.html")

    @cherrypy.expose
    def ventanear(self):
        lista_ventana = self.transporte.puestos_libres_ventana()
        return str(lista_ventana)

    @cherrypy.expose
    def puestos_pasillo(self):
        return open("views/puestos_disponibles_pasillo.html")
    
    @cherrypy.expose
    def pasillar(self):
        lista_pasillo = self.transporte.puestos_libres_pasillo()
        return str(lista_pasillo)
    
    @cherrypy.expose
    def lista_pasajeros(self): # este es href en index.html
        return open("views/pasajeros_en_bus.html")

    @cherrypy.expose
    def mostrar_pasajeros(self): # esta es la action en el archivo pasajeros_en_bus.html
        lista = self.transporte.listar_pasajeros()
        return str(lista)


if __name__=="__main__":
    cherrypy.quickstart(Comercializar())
