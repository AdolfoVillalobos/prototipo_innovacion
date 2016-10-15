import random
import xlsxwriter as xls

#LISTA DE ARBOLES
def posiciones_arboles(filas,filainicial,filafinal):
	arboles=list()
	for x in filas:
		y=filainicial
		fila_arboles=list()
		while y < filafinal+1:
			arbol=[[x,y],[x,y+1]]
			fila_arboles.append(arbol)
			y=y+2
		arboles.append(fila_arboles)
	return arboles

filas=[3,4,9,10,15,16,21,22,27,28,33,34,39,40,45,46]
filainicial=3
filafinal=48
arboles=posiciones_arboles(filas,filainicial,filafinal) #lista que tiene por elemento cada fila de arboles que a su vez tiene 



def posicion_nueva(posicion_anterior,posicion_actual):
	mov=random.randint(0,650)
	x=posicion_actual[0]
	y=posicion_actual[1]
	#se qe fue para afuera porque mi posicion actual x aumento o porque mi posicion en y disminuyo
	posibles_movimientos=[[x-1,y-1],[x,y-1],[x+1,y-1],[x-1,y],[x,y],[x+1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
	if x> posicion_anterior[0] or y< posicion_anterior[1]:
		if mov <= 641:
			posicion_new=posicion_anterior
		if mov==642:
			posicion_new=posibles_movimientos[0]
		if mov==643:
			posicion_new=posibles_movimientos[1]
		if mov==644:
			posicion_new=posibles_movimientos[2]
		if mov==645:
			posicion_new=posibles_movimientos[3]
		if mov==646:
			posicion_new=posibles_movimientos[4]
		if mov==647:
			posicion_new=posibles_movimientos[5]
		if mov==648:
			posicion_new=posibles_movimientos[6]
		if mov==649:
			posicion_new=posibles_movimientos[7]
		if mov==650:
			posicion_new=posibles_movimientos[8]

	else: 
		if mov <= 640:
			posicion_new=posibles_movimientos[4]
		if mov<=643 and mov>640:
			posicion_new=posibles_movimientos[7]
		if mov==644:
			posicion_new=posibles_movimientos[0]
		if mov==645:
			posicion_new=posibles_movimientos[1]
		if mov==646:
			posicion_new=posibles_movimientos[2]
		if mov==647:
			posicion_new=posibles_movimientos[3]
		if mov==648:
			posicion_new=posibles_movimientos[5]
		if mov==649:
			posicion_new=posibles_movimientos[6]
		if mov==650:
			posicion_new=posibles_movimientos[8]
	return posicion_new	


#MOVIMIENTOS

def mov_trabajadorx (posicion_inicial,dimensionx,dimensiony):
	x=posicion_inicial[0]
	y=posicion_inicial[1]
	posicion_anterior=posicion_inicial
	posicion_actual=posicion_inicial
	movimientosfinales=list()
	tiempo=0
	while tiempo <7200:
		posicion_siguiente=posicion_nueva(posicion_anterior,posicion_actual)
		puedemoverse=True
		for columna in arboles:
			for arbol in columna:
				if arbol[0]==posicion_siguiente or arbol[1]==posicion_siguiente:
					puedemoverse=False 
		if posicion_siguiente[0]<0 or posicion_siguiente[1]<0:
			puedemoverse=False
		if posicion_siguiente[0]>dimensionx or posicion_siguiente[1]>dimensiony:
			puedemoverse=False
		if puedemoverse == True:
			movimientosfinales.append(posicion_siguiente)
			tiempo=tiempo+1
			posicion_anterior=posicion_actual
			posicion_actual=posicion_siguiente
	return movimientosfinales


#para trabajador 1 
lista=(((5,3),(19,3)),((26,3) ,(12,3)),((33,3),(12,3)))


dimensionx=50
dimensiony=50
#tiemporeal_trabajadorx=mov_trabajadorx(posicion_inicial,dimensionx,dimensiony)



####

#Parametros
import pandas as pd
import time
import datetime
from datetime import date

#Parametros

cantidad_dias = 2
cantidad_trabajadores = 3
paso_muestreo =5
cantidad_horas = 10
cantidad_muestreado = 60*60*cantidad_horas/paso_muestreo

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
		posicion_inicial = lista[i][k]
		tiemporeal_trabajadorx=mov_trabajadorx(posicion_inicial,dimensionx,dimensiony)
		horainicio =datetime.datetime(2016, 10, 11, 8, 0)
		worksheet = workbook.add_worksheet("Trabajador "+str(ID[i])+" dia "+ str(k))
#Inicio de la Tabla
		col = 0
		for item in tabla:
			worksheet.write(0,col,item)
			col+=1
#Llenado ID,Nombre,Fecha y Horas
		delta = datetime.timedelta(seconds=paso_muestreo)
		for j in range(1,cantidad_muestreado):
			horainicio+=delta
			worksheet.write(j,0,ID[i])
			worksheet.write(j,1,Nombres[i])
			worksheet.write(j,2,fechas[k].strftime("%Y-%m-%d"))
			worksheet.write(j,3,horainicio.strftime("%H:%M:%S"))
			worksheet.write(j,4,tiemporeal_trabajadorx[j][1])
			worksheet.write(j,5,tiemporeal_trabajadorx[j][0])
workbook.close()









