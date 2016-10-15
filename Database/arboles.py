filas=[3,4,9,10,15,16,21,22,27,28,33,34,39,40,45,46]
arboles=list()
for x in filas:
	y=3
	fila_arboles=list()
	while y < 49:
		arbol=[[x,y],[x,y+1]]
		fila_arboles.append(arbol)
		y=y+2
	arboles.append(fila_arboles)












