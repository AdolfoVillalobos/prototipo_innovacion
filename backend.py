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
		
	

direccion1 = "Database/database.xlsx"
direccion2 = "Database/trabajadores.xls"
b = BackEnd(direccion1,direccion2)
b.crear_trabajadores(2)