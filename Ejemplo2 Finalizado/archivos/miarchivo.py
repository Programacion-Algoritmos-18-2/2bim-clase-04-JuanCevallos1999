import codecs 
class MiArchivo: #Creamos la clase Archivo para abrir uno
 
    def __init__(self): #Constructor 

        self.archivo = codecs.open("data/informacion.csv", "r") #Abre el archivo y lo lee como atributo  por "r"

    def obtener_informacion(self): #Lee las lineas 
        return self.archivo.readlines() #devuelve las lineas

    def cerrar_archivo(self):  #Cerramos el archivo
        self.archivo.close()

class MiArchivoEscribir: #Creamos la clase para escribir el archivo
#
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/info2.csv", "a") #Que vaya a esta direccon y sino existe lo crea y añade lo que agrego al finla del archivo

    def agregar_informacion(self, e): #Recibe un parametro de tipo equipo y lo escribe con los atributos del objeto 
        self.archivo.write("%s-%s-%d-%d\n" % (e.nombre, e.ciudad, e.campeonatos, e.numJugadores))
    
    def cerrar_archivo(self): #Cierra el archivo
        self.archivo.close()