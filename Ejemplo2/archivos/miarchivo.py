import codecs 
class MiArchivo:

    def __init__(self):

        self.archivo = codecs.open("data/informacion.csv", "r") #Abre el archivo y lo lee

    def obtener_informacion(self): #Lee las lineas 
        return self.archivo.readlines()

    def cerrar_archivo(self): 
        self.archivo.close()

class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/info2.csv", "a") #Que vaya a esta direccon y sino existe lo crea y añade lo que agrego al finla del archivo

    def agregar_informacion(self, e): #Recibe un parametro de tipo equipo
        self.archivo.write("%s-%s-%d-%d\n" % e.nombre, e.ciudad, e.campeonatos, e.numJugadores)
    
    def cerrar_archivo(self):
        self.archivo.close()