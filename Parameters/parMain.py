"""
 This file holds all Parameter calculation functions
 parMain(fileName) is the summation function and returns a numpy array of the four parameters
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def avg(pList):
    """Returns the average value of the given list"""

    aver = pList[-1]

    for i in range(len(pList) - 1):

        aver += pList[i]

    return aver / len(pList)

def linRegress(pList):
    """Returns the slope of the line created by linear regression"""

    w, h = 1, len(pList)

    xx = [[0 for x in range(w)] for y in range(h)]

    count = 0

    for i in range(len(pList)):
        count = count + 1
        xx[i][0] = count

    model = LinearRegression().fit(xx, pList)

    return model.coef_

def parameter1(volList):
    """Determines percent volatility based on volume by finding average daily change and dividing that by average volume"""

    volaAvg = 0

    for i in range(len(volList) - 1):
        volaAvg += abs( volList[i] - (volList[i + 1]) )
        
    volaAvg = volaAvg / (len(volList) - 1)

    volaPercent = volaAvg / avg(volList) 

    return volaPercent * 100

def parameter2(priceList):
    """Determines percent volatility based on price by finding average daily change and dividing that by average price"""

    volaAvg = 0

    for i in range(len(priceList) - 1):
        volaAvg += abs( priceList[i] - (priceList[i + 1]) )

    volaAvg = volaAvg / (len(priceList) - 1)
    volaPercent = volaAvg / avg(priceList)

    return volaPercent * 100

def parameter3(priceList):
    """Determines slope of three 10-day averaged points, and returns as a percent of average stock price"""

    firAvg = sum(priceList[:10])
    midAvg = sum(priceList[ (len(priceList)) - 5:(len(priceList)) + 5])
    lasAvg = sum(priceList[-10:])

    firAvg = firAvg / 10
    midAvg = midAvg / 10
    lasAvg = lasAvg / 10

    avgs = np.array(([firAvg, midAvg, lasAvg]))
    slope = linRegress(priceList)
    adjSlope = slope / avg(priceList)

    return adjSlope * 100

def parameter4(priceList):
    """Determines the slope found by linear regression, and returns as a percent of average stock price."""

    slope = linRegress(priceList)
    adjSlope = slope / avg(priceList)

    return adjSlope * 100

def parMain(fileName):
	"""Calls parameter 1 through 4 and returns the four parameters into a numpy array"""
	colnames = ['date', 'value', 'high', 'low', 'open', 'close', 'volume', 'adjClose']
	csvFile = pd.read_csv(fileName, names = colnames, skiprows = 1)
	value = csvFile.value.tolist()
	volume = csvFile.volume.tolist()
	
	volaVol = parameter1(volume)
	volaPrice = parameter2(value)
	tenDayLinreg = parameter3(value)
	linreg = parameter4(value)

	pars = [volaVol, volaPrice, tenDayLinreg, linreg]

	return pars
