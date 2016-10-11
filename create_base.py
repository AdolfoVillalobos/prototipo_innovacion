import xlsxwriter as xls

workbook = xls.Workbook("database.xlsx")
worksheet = workbook.add_worksheet()

col = 0

tabla = ("ID","Nombre","Fecha","Hora","Pos_X","Pos_Y")

for item in tabla:
	worksheet.write(0,col,item)
	col+=1

workbook.close()