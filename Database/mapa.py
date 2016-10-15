
import matplotlib.pyplot as plt
import numpy as np

def plot(lista,posiciones):


	nrows, ncols = 50,50
	image = np.zeros((nrows,ncols))

	row_labels = range(nrows)
	col_labels = range(ncols)
	for l in range(100):
		for i in lista:
			for j in i:
				for k in j:
					image[k[1],k[0]]=1
		image[posiciones[l][1],posiciones[l][0]]=2
		plt.matshow(image)
		plt.xticks(range(ncols), col_labels)
		plt.yticks(range(nrows), row_labels)
		plt.show()
		image[posiciones[l]]=0