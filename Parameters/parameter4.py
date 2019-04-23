#This parameter is simple regression

#import sys
#sys.path.insert(0, '/Users/matthewjones/Desktop/CS307FinProj/FinalProj/Regression')

import linReg
import numpy as np

def parameter4( priceList ):

	x = np.array([])
	count = 0

	for i in range(len(priceList)):

		count = count + 1
		x = np.append(x, [count])

	slope, yInter = linReg.linReg(x, priceList, alpha=0.0000001, epochs=10000)

	return slope

#hold = parameter4(np.array([1,2, 2, 4, 6, 6, 9, 10]))
