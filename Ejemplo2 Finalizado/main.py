from archivos.miarchivo import *
from modelo.modelado import *   #Importamos las clases necesarias 
archivo = MiArchivo() 		#Creamos los objetos que utilizaremos
archivo2 = MiArchivoEscribir()
lista = archivo.obtener_informacion()
lista = [l.split("|") for l in lista]  #Creamos una lista con cada una de las listas
lista_equipo = []  #Creamos una lista vacia que contendra objetos 
for d in lista: #Creamos objetos de tipo equipo con cada uno de los parametros 
    e = Equipo(d[0], d[1], d[2], d[3])
    lista_equipo.append(e) #Creamos una lista de objetos equipo
operacion = Operaciones(lista_equipo)  #Creamos el objeto para operar y enviamos la lista de objetos
a = int(input("1. Nombres \t Otro.Campeonatos"))  #Damos las opciones de menú
if (a==1): 
	lista2 = operacion.ordenarNombre()  #Si es 1 ordenamos por nombre
else:
	lista2 = operacion.ordenarCampeonato()	#Si es 2 ordenamos por campeonato
for d in lista2:						#Usamos un for para enviar uno por uno los objetos al archivo
	archivo2.agregar_informacion(d)  #Escribimos el archivo
archivo2.cerrar_archivo() #Cerramos el archivo
