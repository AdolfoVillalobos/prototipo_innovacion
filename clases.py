import numpy as np

class Trabajador:
	def __init__(self,ID,posx,posy):
		self.ID=ID
		self.posx=posx
		self.posy=posy
		self.árbol_actual = []


class Arbol:
	def __init__(self,posx,posy):
		self.capacidad = 100
		self.estado_actual = 0
		self.pos = []


