import numpy as np

class Trabajador:
	def __init__(self,ID,posx,posy):
		self.ID=ID
		self.posx=posx
		self.posy=posy
		self.productividad_promedio = 0
		self.productividades_diarias = dict()
		self.arbol_actual = []
		self.lista_posiciones_x =[]
		self.lista_posiciones_y =[]
	def actualizar_productividades_diarias(self,dia,hora,produccion):
		self.productividades_diarias[(dia,hora)] = produccion
	def calcular_productividad(self):
		keys = self.productividades_diarias.keys()
		sum = 0.0
		for i in keys:
			sum += self.productividades_diarias[i]
		sum = sum/n
		return (sum)
	def actualizar_lista_posiciones(self,lista_x,lista_y):
		self.lista_posiciones_x=lista_x
		self.lista_posiciones_y=lista_y


class Arbol:
	def __init__(self,posx,posy):
		self.capacidad = 100
		self.estado_actual = 0
		self.pos = []



