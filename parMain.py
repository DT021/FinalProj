import pandas as pd
import numpy as np
from Regression import linReg
# import parameter1 as p1
# import parameter2 as p2
# import parameter3 as p3
# import parameter4 as p4
import glob
import sys

def parameter1(volList):

    avg = volList[-1]
    volaAvg = 0

    for i in range(len(volList) - 1):
        volaAvg += abs( volList[i] - (volList[i + 1]) )
        
        avg += volList[i]
        
    avg = avg / len(volList)
    volaAvg = volaAvg / (len(volList) - 1)

    volaPercent = volaAvg / avg 

    return volaPercent

def parameter2(priceList):

        avg = priceList[-1]
        volaAvg = 0

        for i in range(len(priceList) - 1):
                volaAvg += abs( priceList[i] - (priceList[i + 1]) )

                avg += priceList[i]

        avg = avg / len(priceList)
        volaAvg = volaAvg / (len(priceList) - 1)

        volaPercent = volaAvg / avg

        return volaPercent

def parameter3(priceList):

    firAvg = sum(priceList[:10])
    midAvg = sum(priceList[ (len(priceList)) - 5:(len(priceList)) + 5])
    lasAvg = sum(priceList[-10:])

    firAvg = firAvg / 10
    midAvg = midAvg / 10
    lasAvg = lasAvg / 10

    avgs = np.array(([firAvg, midAvg, lasAvg]))
    x = np.array(([1,2,3]))

    linModel = linReg.LinearRegression(x, avgs)
    linModel.fitData()


    return (avgs[-1] - avgs[0]) / 2

def parameter4(priceList):

    x = np.array([])
    count = 0

    for i in range(len(priceList)):

        count = count + 1
        x = np.append(x, [count])

    linModel = linReg.LinearRegression(x, priceList)
    linModel.fitData()

    return (priceList[-1] - priceList[0]) / (x[-1] - x[0]) 

def parMain(fileName):

	colnames = ['date', 'value', 'high', 'low', 'open', 'close', 'volume', 'adjClose']
#        csvFile = pd.read_csv('../Data/'+fileName, names = colnames, skiprows = 1)
	csvFile = pd.read_csv(fileName, names = colnames, skiprows = 1)
#	date = csvFile.date.tolist()
	value = csvFile.value.tolist()
#	high = csvFile.high.tolist()
#	low = csvFile.low.tolist()
#	open = csvFile.open.tolist()
#	close = csvFile.close.tolist()
	volume = csvFile.volume.tolist()
#	adjClose = csvFile.adjClose.tolist()
	
	volaVol = parameter1(volume)
	volaVal = parameter2(value)
	buyTenDayLinreg = parameter3(value)
	buyLinreg = parameter4(value)

	pars = [volaVol, volaVal, buyTenDayLinreg, buyLinreg]

#	print("P1 THOURHG P4\n")
#	print( volaVol, volaVal, buyTenDayLinreg, buyLinreg)

	return pars
#Probably should return all params as a list for easy writing to file
	#return volParam
#fileListSP = glob.glob("Data/*.csv")
#fileListVol = glob.glob("VolData/*.csv")
#print(parMain("studentData/test.csv"))
# List all files in the Data Directory
"""fileListSP = glob.glob("../Data/*.csv")
fileListVol = glob.glob("../VolData/*.csv")

openFile = open(r"params.txt", "a")

#print("CHECK2")

count = 0

for fileName in fileListSP:
	
	count = count + 1
#	print(count)
	
	parsSP = parMain(fileName)
#	L = ["count: ",  str(count), " P1: ", str(parsSP[0]), " P2: ", str(parsSP[1]), " P3: ", str(parsSP[2]), " P4: ", str(parsSP[3]), "\n"]
	
    parsSP[0] = parsSP[0]*100
    parsSP[1] = parsSP[1]*100
    parsSP[2] = parsSP[2]*100
    parsSP[3] = parsSP[3]/10

    volTotal = parsSP[0]+parsSP[1]
    valTotal = parsSP[2]+parsSP[3]

    if (volTotal > 4) and (valTotal > 50):
        L = [str(parsSP[0]), " ", str(parsSP[1]), " ", str(parsSP[2]), " ", str(parsSP[3]), " Volatile-Gain", "\n"]
    elif (volTotal > 4) and (valTotal < 50):
        L = [str(parsSP[0]), " ", str(parsSP[1]), " ", str(parsSP[2]), " ", str(parsSP[3]), " Volatile-Loss", "\n"]
    elif (volTotal < 4) and (valTotal > 50):
        L = [str(parsSP[0]), " ", str(parsSP[1]), " ", str(parsSP[2]), " ", str(parsSP[3]), " Stable-Gain", "\n"]
    elif (volTotal < 4) and (valTotal < 50):
        L = [str(parsSP[0]), " ", str(parsSP[1]), " ", str(parsSP[2]), " ", str(parsSP[3]), " Stable-Loss", "\n"]

            #	print("L IS PRINTED\n")
            #	print(L)

            openFile.writelines(L)

count = 0

for fileName in fileListVol:
	
	count = count + 1
#	print(count)

	parsVol = parMain(fileName)
        
        parsVol[0] = parsVol[0]*100
        parsVol[1] = parsVol[1]*100
        parsVol[2] = parsVol[2]*100
        parsVol[3] = parsVol[3]/10

        volTotal = parsVol[0]+parsVol[1]
        valTotal = parsVol[2]+parsVol[3]

        if (volTotal > 4) and (valTotal > 50):
            L = [str(parsVol[0]), " ", str(parsVol[1]), " ", str(parsVol[2]), " ", str(parsVol[3]), " Volatile-Gain", "\n"]
        elif (volTotal > 4) and (valTotal < 50):
            L = [str(parsVol[0]), " ", str(parsVol[1]), " ", str(parsVol[2]), " ", str(parsVol[3]), " Volatile-Loss", "\n"]
        elif (volTotal < 4) and (valTotal > 50):
            L = [str(parsVol[0]), " ", str(parsVol[1]), " ", str(parsVol[2]), " ", str(parsVol[3]), " Stable-Gain", "\n"]
        elif (volTotal < 4) and (valTotal < 50):
            L = [str(parsVol[0]), " ", str(parsVol[1]), " ", str(parsVol[2]), " ", str(parsVol[3]), " Stable-Loss", "\n"]

	openFile.writelines(L)

openFile.close()

sys.exit()
"""