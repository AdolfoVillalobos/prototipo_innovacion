import xlsxwriter as xls


#Iniciar el  archivo Excel y crear un Datasheet para el trabajador

workbook = xls.Workbook("database.xlsx")
worksheet = workbook.add_worksheet()


#Inicio de la Tabla
col = 0
tabla2 = ("ID","Nombre","Fecha","Hora","Pos_X","Pos_Y")

for item in tabla2:
	worksheet.write(0,col,item)
	col+=1

#Llenado de Tabla:







workbook.close()