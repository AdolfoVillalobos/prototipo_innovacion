import xlsxwriter as xls
import pandas as pd
import time
import datetime
from datetime import date
import numpy as np

#Parametros
cantidad_dias = 2
cantidad_trabajadores = 3
paso_muestreo =5
cantidad_horas = 10
cantidad_muestreado = 60*60*cantidad_horas/paso_muestreo


#Abrir base de datos
workbook = xls.Workbook("database.xlsx")


#crear Mapa

nrows, ncols = 21,21
image = np.zeros((nrows,ncols))


#Coordenadas Arboles
def generar_arboles(ncols,nrows,image):
	arboles = []
	paso = 3
	for i in range( ncols/3):
		image[2:nrows-2,3*i+1] = np.ones((ncols-4,))
		