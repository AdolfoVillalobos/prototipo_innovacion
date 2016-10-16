import numpy as np
import random as rd

tiempos = [10+rd.randint(-2,2) for i in range(10)]

class Trabajador:
	def __init__(self,ID,nombre,posx,posy):
		self.ID=ID
		self.nombre=nombre
		self.posx=posx
		self.posy=posy
		self.productividad_promedio = 10
		self.productividades_diarias = dict()
		self.arbol_actual = []
		self.lista_posiciones_x =[self.posx]
		self.lista_posiciones_y =[self.posy]
	def anadir_dia_de_productividad(self,dia,lista):
		self.productividades_diarias[dia]=lista
	def obtener_productividades_diarias(self,dia):
		print "ouch"
	def calcular_productividad(self):
		n = len(self.productividades_diarias)
		keys = self.productividades_diarias.keys()
		suma = 0.0
		for i in keys:
			suma += sum(self.productividades_diarias[i])
		suma = suma/(10.0*n)
		self.productividad_promedio = suma
		return (suma)

class Arbol:
	def __init__(self,posx,posy):
		self.capacidad = 100
		self.estado_actual = 0
		self.pos = []


