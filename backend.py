import clases
import xlsxwriter as xls
import pandas as pd
import time
import datetime
from datetime import date
import random as rd
import matplotlib.pyplot as plt

tiempos = [10+rd.randint(-2,2) for i in range(10)]
class BackEnd:
	def __init__(self,database, direccion_trabajadores):
		self.dias = 2
		self.database = database
		self.parsed_database=dict()
		self.direccion_trabajadores = direccion_trabajadores
		self.trabajadores = []
	def parse_database(self):
		dicti = dict()
		excel_base = pd.ExcelFile(self.database)
		for i in range(self.dias):
			for j in range (len(self.trabajadores)):
				dt = excel_base.parse("Trabajador "+str(self.trabajadores[j].ID)+" dia "+ str(i))
				dicti[(i,j)]=dt
		self.parsed_database = dicti
	def crear_trabajadores(self,numero):
		excel_trabajadores = pd.ExcelFile(self.direccion_trabajadores)
		dt = excel_trabajadores.parse("Sheet1")
		ID = dt['ID']
		Nombre = dt["Nombre"]
		for i in range(numero):
			trabajadorcito = clases.Trabajador(ID[i],str(Nombre[i]),0,0)
			self.trabajadores.append(trabajadorcito)
	def cargar_posiciones(self,hora,dia):
		for i in self.trabajadores:	
			str_hora = [str(x) for x in self.parsed_database[(dia,i.ID)]['Hora']]
			m = str_hora.index(hora)
			x,y = self.parsed_database[(dia,i.ID)]['Pos_X'][m], self.parsed_database[(dia,i.ID)]['Pos_Y'][m]
			i.posx = x
			i.posy = y
		print "Se han cargado las posiciones" 
	def calcular_productividades (self,dia,lista):
		for i in self.trabajadores:
			i.anadir_dia_de_productividad(dia,lista)
	def calcular_promedios(self):
		promedios_actuales = dict()
		for i in self.trabajadores:
			i.calcular_productividad()
			promedios_actuales[i.ID] = i.productividad_promedio
	def prediccion_a_cantidad_fija(self,dias,n_horas_diaria,cantidad):
		cuanto_produzco = 0
		coef = dias*n_horas_diaria
		for i in self.trabajadores:
			cuanto_produzco+=i.productividad_promedio*coef
		return cuanto_produzco
	def lista_mejores_trabajadores(self):
		result = [(i.ID,i.nombre,i.productividad_promedio) for i in self.trabajadores]
		result = sorted(result,key=lambda x:x[2],reverse=True)
		return result
	def obtener_grafico_productividades(self,trabajador,dia,nombre_archivo):
		x = (9,10,11,12,13,14,15,16,17,18)
		z = self.trabajadores[trabajador].productividades_diarias[dia]
		plt.bar(x, z, 1, color="blue")
		plt.show()

direccion1 = "Database/database.xlsx"
direccion2 = "Database/trabajadores.xls"
b = BackEnd(direccion1,direccion2)
b.crear_trabajadores(3)
b.parse_database()
b.calcular_productividades(0,tiempos)