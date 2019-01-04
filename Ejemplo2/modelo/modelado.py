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

class Operaciones:

	def __init__(self, listado):
		self.listado_equipo = listado

	def ordenar(self):		
		return sorted(self.listado_equipo, key=lambda equipo: equipo.getNombre())
