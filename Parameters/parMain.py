import pandas as pd
import numpy as np
from Regression import linReg
from sklearn.linear_model import LinearRegression

def avg(pList):
    """Return the average value of the given list."""

    aver = pList[-1]

    for i in range(len(pList) - 1):

        aver += pList[i]

    return aver / len(pList)

def linRegress(pList):
    """Return the slope of the line created by linear regression."""

    w, h = 1, len(pList)

    xx = [[0 for x in range(w)] for y in range(h)]

    count = 0

    for i in range(len(pList)):
        count = count + 1
        xx[i][0] = count

    model = LinearRegression().fit(xx, pList)

    return model.coef_

def parameter1(volList):
    """Determine percent volatility based on volume."""

    avg = volList[-1]
    volaAvg = 0

    for i in range(len(volList) - 1):
        volaAvg += abs( volList[i] - (volList[i + 1]) )
        
        avg += volList[i]
        
    avg = avg / len(volList)
    volaAvg = volaAvg / (len(volList) - 1)

    volaPercent = volaAvg / avg 

    return volaPercent * 100

def parameter2(priceList):
    """Determine percent volatility based on price."""

    avg = priceList[-1]
    volaAvg = 0

    for i in range(len(priceList) - 1):
        volaAvg += abs( priceList[i] - (priceList[i + 1]) )

        avg += priceList[i]

    avg = avg / len(priceList)
    volaAvg = volaAvg / (len(priceList) - 1)
    volaPercent = volaAvg / avg

    return volaPercent * 100

def parameter3(priceList):
    """Determine slope of three 10 day moving average, and return as a percent 
    of average stock price."""

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
    """Determine the slope found by linear regression, and return as a percent of 
    average stock price."""

    slope = linRegress(priceList)
    adjSlope = slope / avg(priceList)

    return adjSlope * 100

def parMain(fileName):

	colnames = ['date', 'value', 'high', 'low', 'open', 'close', 'volume', 'adjClose']
	csvFile = pd.read_csv(fileName, names = colnames, skiprows = 1)
	value = csvFile.value.tolist()
	volume = csvFile.volume.tolist()
	
	volaVol = parameter1(volume)
	volaVal = parameter2(value)
	buyTenDayLinreg = parameter3(value)
	buyLinreg = parameter4(value)

	pars = [volaVol, volaVal, buyTenDayLinreg, buyLinreg]

	return pars
