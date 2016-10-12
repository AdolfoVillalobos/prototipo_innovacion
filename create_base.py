import xlsxwriter as xls
import pandas as pd
import time
import datetime
from datetime import date

#Parametros

cantidad_dias = 2
cantidad_trabajadores = 3
terreno_x = 100
terreno_y = 100
cantidad_muestreado = 60*60*8/5

#Fechas
fechainicio = date(2016,10,11)
fechas = []
for i in range(cantidad_dias):
	delta = datetime.timedelta(days=1)
	fechainicio+=delta
	fechas.append(fechainicio)
	


#Recuperar trabajadores (No toda la info disponible)
trabajadores = pd.ExcelFile("trabajadores.xls")
dt = trabajadores.parse("Sheet1")
ID = dt['ID']
Nombres = dt['Nombre']
#Iniciar el  archivo Excel y crear un Datasheet para el trabajador

workbook = xls.Workbook("database.xlsx")
tabla = ("ID","Nombre","Fecha","Hora","Pos_X","Pos_Y")
for k in range(cantidad_dias):
	for i in range(cantidad_trabajadores):
		worksheet = workbook.add_worksheet("Trabajador "+str(ID[i])+" dia "+ str(k))
#Inicio de la Tabla
		col = 0
		for item in tabla:
			worksheet.write(0,col,item)
			col+=1
#Llenado ID,Nombre,Fecha y Horas
		for j in range(1,cantidad_muestreado):
			worksheet.write(j,0,ID[i])
			worksheet.write(j,1,Nombres[i])
			worksheet.write(j,2,fechas[k].strftime("%Y-%m-%d"))
			worksheet.write(j,3,)
workbook.close()