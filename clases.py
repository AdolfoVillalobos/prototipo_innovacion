import numpy as np

class Trabajador:
	def __init__(self,ID,posx,posy):
		self.ID=ID
		self.posx=posx
		self.posy=posy
		self.productividad_promedio = 0
		self.productividades_diarias = dict()
		self.arbol_actual = []
		self.lista_posiciones_x =[self.posx]
		self.lista_posiciones_y =[self.posy]
	def calcular_productividades_hora(self):

	def calcular_productividad(self):
		keys = self.productividades_diarias.keys()
		suma = 0.0
		for i in keys:
			suma += self.productividades_diarias[i]
		suma = suma/n
		self.productividad_promedio = sum
		return (sum)

class Arbol:
	def __init__(self,posx,posy):
		self.capacidad = 100
		self.estado_actual = 0
		self.pos = []



