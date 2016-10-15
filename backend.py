import clases
import xlsxwriter as xls
import pandas as pd

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
		for i in range(numero):
			trabajadorcito = clases.Trabajador(ID[i],0,0)
			self.trabajadores.append(trabajadorcito)
	def cargar_posiciones(self,hora,dia):
		for i in self.trabajadores		
			m = self.parsed_database[(dia,i.ID)]['Hora'].index(hora)
			x,y = self.parsed_database[(dia,i.ID)]['Pos_X'][m], self.parsed_database[(dia,i.ID)]['Pos_y'][m]
			trabajadores[i].posx = x
			trabajadores[i].posy = y
		print "Se han cargado las posiciones"
	def calcular_productividades (self,hora,dia):
		print "Las productividades han sido calculadas, para cada trabajador"
	def calcular_promedios(self):
		for i in trabajadores:
			i.calcular_promedios()
	

direccion1 = "Database/database.xlsx"
direccion2 = "Database/trabajadores.xls"
b = BackEnd(direccion1,direccion2)
b.crear_trabajadores(2)