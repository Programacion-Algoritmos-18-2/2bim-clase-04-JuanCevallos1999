class Equipo(object): 
#Constructor de la clase equipo con 4 parametros
	def __init__(self, n, a, e ,p):

		self.nombre = n
		self.ciudad = a
		self.campeonatos = int(e)
		self.numJugadores = int(p)
#Metodos set y get de los atributos
	def setNombre(self, n):
		self.nombre = n

	def getNombre(self):
		return self.nombre

	def setCiudad(self, n):
		self.ciudad = n

	def getCiudad(self):
		return self.ciudad

	def setCampeonatos(self, n):
		self.campeonatos = int(n)

	def getCampeonatos(self):
		return self.campeonatos

	def setNumJugadores(self, n):
		self.numJugadores = int(n) 

	def getNumJugadores(self):
		return self.numJugadores

	def __str__ (self):
		return "-%s-%s-%d-%d\n" % (self.getNombre(), self.getCiudad(),self.getCampeonatos(), self.getNumJugadores())
	
	def __repr__(self): #Metodo similar a str pero para metodos sorted
		return "%s - %s - %d - %d\n" % (self.getNombre(), self.getCiudad(),self.getCampeonatos(), self.getNumJugadores())
#Clase operaciones
class Operaciones:
#Creamos el constructor que recibira la lista de objetos que creamos
	def __init__(self, listado):
		self.listado_equipo = listado
#Metodo para ordenar por nombre
	def ordenarNombre(self):		
		return sorted(self.listado_equipo, key=lambda equipo: equipo.getNombre())  #Utilizamos la funcion de python para ordenar por nombre
#Metodo para ordenar por campeonato
	def ordenarCampeonato(self):		
		return sorted(self.listado_equipo, key=lambda equipo: equipo.getCampeonatos())
#Utilizamos la funcion de python para ordenar 