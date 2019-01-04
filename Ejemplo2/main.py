from archivos.miarchivo import *
from modelo.modelado import *
archivo = MiArchivo()
archivo2 = MiArchivoEscribir()
lista = archivo.obtener_informacion()
lista = [l.split("|") for l in lista]
lista_equipo = []
for d in lista:
    # print(d)
    e = Equipo(d[0], d[1], d[2], d[3])
    #print (p)
    #archivo2.agregar_informacion(e)
    lista_equipo.append(e)

operacion = Operaciones(lista_equipo)
#operacion.ordenar()

print(operacion.ordenar())
#print (lista_equipo)