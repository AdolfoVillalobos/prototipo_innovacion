import numpy as np

class Trabajador:
	def __init__(self,ID,posx,posy):
		self.ID=ID
		self.posx=posx
		self.posy=posy
		self.productividad_promedio = 0
		self.productividades_diarias = dict()
		self.arbol_actual = []
	def actualizar_productividades_diarias(self,dia,hora,produccion):
		self.productividades_diarias[(dia,hora)] = produccion
	def calcular_productividad(self):
		keys = self.productividades_diarias.keys()
		sum = 0
		for i in keys:
			sum += self.productividades_diarias[i]
		return (sum)

class Arbol:
	def __init__(self,posx,posy):
		self.capacidad = 100
		self.estado_actual = 0
		self.pos = []



