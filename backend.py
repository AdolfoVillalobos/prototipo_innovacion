import clases
import xlsxwriter as xls
import pandas as pd
import time
import datetime
from datetime import date
import random as rd
class BackEnd:
	def __init__(self,database, direccion_trabajadores):
		self.dias = 2
		self.num_trabajadores=0
		self.database = database
		self.parsed_database=dict()
		self.direccion_trabajadores = direccion_trabajadores
		self.trabajadores = []
		self.productividades_juguete = dict()
#Preliminares. parse_database entrega una base manejable en python, a partir de los excel
	def parse_database(self):
		dicti = dict()
		excel_base = pd.ExcelFile(self.database)
		for i in range(self.dias):
			for j in range (len(self.trabajadores)):
				dt = excel_base.parse("Trabajador "+str(self.trabajadores[j].ID)+" dia "+ str(i))
				dicti[(i,j)]=dt
		self.parsed_database = dicti
	def crear_trabajadores(self,numero,lista_posiciones):
		self.num_trabajadores=numero
		excel_trabajadores = pd.ExcelFile(self.direccion_trabajadores)
		dt = excel_trabajadores.parse("Sheet1")
		ID = dt['ID']
		Nombre = dt["Nombre"]
		Fechas = dt['Fecha Ingreso']
		Rut=dt['Rut']
		Salario = dt['Salario']
		Contrato = dt['Tipo Contrato']
		for i in range(numero):
			trabajadorcito = clases.Trabajador(ID[i],str(Nombre[i]),lista_posiciones[i][0],lista_posiciones[i][1],Fechas[i],str(Contrato[i]),int(Salario[i]),int(Rut[i]))
			self.trabajadores.append(trabajadorcito)
	#Esta rutina se ejecuta todo el rato. Va actualizando las posiciones	
	def cargar_posiciones(self,hora,dia):
		for i in self.trabajadores:	
			str_hora = [str(x) for x in self.parsed_database[(dia,i.ID)]['Hora']]
			m = str_hora.index(hora)
			x,y = self.parsed_database[(dia,i.ID)]['Pos_X'][m], self.parsed_database[(dia,i.ID)]['Pos_Y'][m]
			i.posx = x
			i.posy = y
		print "Se han cargado las posiciones" 
	def calcular_productividades_individual(self,dia,lista,trabajador):
		self.trabajadores[trabajador].anadir_dia_de_productividad(dia,lista)
	
#Cosas bonitas el Modelo:
	def calcular_promedios(self):
		promedios_actuales = dict()
		for i in self.trabajadores:
			i.calcular_productividad()
			promedios_actuales[i.ID] = i.productividad_promedio
	def calcular_promedio_total(self):
		suma = 0.0
		for i in self.trabajadores:
			suma+=i.productividad_promedio
		suma = suma/self.num_trabajadores
		return suma

	def prediccion_a_cantidad_fija(self,dias,n_horas_diaria,cantidad):
		sobran_trabajadores = False
		cuanto_produzco = 0
		coef = dias*n_horas_diaria
		prom =self.calcular_promedio_total()
		for i in self.trabajadores:
			cuanto_produzco+=i.productividad_promedio*coef
		if cantidad >=cuanto_produzco:
			me_Falta = cantidad-cuanto_produzco
			t_necesito = me_Falta/prom
		if cantidad < cuanto_produzco:
			sobran_trabajadores=True
			me_Falta = cantidad-cuanto_produzco
			t_necesito = me_Falta/prom
		return me_Falta,t_necesito,sobran_trabajadores #Cuanto soy capaz de producir, cuantos trabajadores necesito y si me sobran o no

	def lista_mejores_trabajadores(self):
		result = [(i.ID,i.nombre,i.productividad_promedio) for i in self.trabajadores]
		result = sorted(result,key=lambda x:x[2],reverse=True)
		return result
	def lista_trabajadores(self):
 		result = {i.nombre: i.ID for i in self.trabajadores}
 		return result
	def obtener_grafico_productividades(self,trabajador,dia):
		import matplotlib.pyplot as plt
		fig = plt.figure()
		plt.title('Productividad por hora \n'+self.trabajadores[dia].nombre+' dia '+str(dia))
		x = (8,9,10,11,12,13,14,15,16,17)
		z = self.trabajadores[trabajador].productividades_diarias[dia]
		plt.bar(x, z, 1, color="green")
		plt.xlabel('Hora' )
		plt.ylabel('Kilogramos por hora')
		fig.canvas.set_window_title('Grafico de Productividad') 
		plt.show()
	def tabla_trabajadores(self):
		diccionarios = []
		for i in self.trabajadores:
			dicti = dict()
			dicti['ID']=i.ID
			dicti['Nombre']=i.nombre
			dicti['Rut'] = i.rut
			dicti['Salario'] = i.salario
			dicti['Tipo Contrato'] = i.contrato
			dicti['Fecha Contratacion'] = i.fecha.strftime("%Y-%m-%d")
 			dicti['Productividad Promedio'] = i.productividad_promedio
 			diccionarios.append(dicti)
 		return diccionarios
#Esto es para graficar las posiciones en cada instante de tiempo, del trabajador i. la gracia es que no pide la hora, porque en la rutina cargar_posicion ya esta actualizada esa info
	def obtener_posicion(self,i):
		x = self.trabajadores[i].posx
		y = self.trabajadores[i].posy
		return (x,y)
#Modelo Juguete
	def crear_productividades_juguete(self):
		for l in range(self.num_trabajadores):
			for j in range(self.dias):
				tiempos = [30+rd.randint(-3,2) for i in range(10)]
				tiempos[4]=0
				self.productividades_juguete [(j,l)] = tiempos
		#Ahora darselas a cada trabajador
		for k in self.productividades_juguete.keys():
			self.trabajadores[k[1]].productividades_diarias[k[0]]=self.productividades_juguete[k]

direccion1 = "Database/database.xlsx"
direccion2 = "Database/trabajadores.xls"
posiciones = ((3,5),(3,33),(3,26))
b = BackEnd(direccion1,direccion2)
b.crear_trabajadores(3,posiciones)
b.parse_database()
#b.calcular_productividades(0,tiempos)
b.crear_productividades_juguete()