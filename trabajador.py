import numpy as np

class Trabajador:
	def __init__(self,ID,posx,posy):
		self.ID=ID
		self.posx=posx #actual
		self.posy=posy #actual
		self.árbol_actual = []
		self.posiciones = []
		self.productividad = 0
		self.lista_productividades = dict() #Por dia




class Arbol:
	def __init__(self,posx,posy):
		self.capacidad = 10
		self.estado_actual = 0
		self.pos = []


