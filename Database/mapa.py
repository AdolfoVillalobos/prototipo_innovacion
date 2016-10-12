
import matplotlib.pyplot as plt
import numpy as np

# Make a 9x9 grid...
nrows, ncols = 21,21
image = np.zeros((nrows,ncols))


for i in range(7):	
	image[2:nrows-2,3*i+1] =np.ones((ncols-4,))


row_labels = range(nrows)
col_labels = range(ncols)
plt.matshow(image)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
plt.show()