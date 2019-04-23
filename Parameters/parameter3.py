# This parameter is regression with 3 averaged data points
# This first data point is the first 10 days averaged, the second is
# the middle 10 days averaged, and the third is the last 10 days averaged

import numpy as np

#import sys
#sys.path.insert(0, '/Users/matthewjones/Desktop/CS307FinProj/FinalProj/Regression')

import linReg 

# This parameter calculates the regression that occurs from taking the average of the first 10 days,
# the average point of the middle 10 days, and the average point of the last 10 days

def parameter3( priceList ):

	firAvg = sum(priceList[:10])
	midAvg = sum(priceList[ (len(priceList)) - 5:(len(priceList)) + 5])
	lasAvg = sum(priceList[-10:])

	firAvg = firAvg / 10
	midAvg = midAvg / 10
	lasAvg = lasAvg / 10

	avgs = np.array(([firAvg, midAvg, lasAvg]))
	x = np.array(([1,2,3]))

	slope, yInter = linReg.linReg(x, avgs, alpha=0.0000001, epochs=10000)

	return slope


#slopeHolde = parameter3(np.array(([0, 1, 9, 9, 9, 2, 3, 9, 9, 9, 4, 5])))
