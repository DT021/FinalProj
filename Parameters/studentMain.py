import pandas as pd
import numpy as np
import parameter1 as p1
import parameter2 as p2
import parameter3 as p3
import parameter4 as p4
import glob
import sys

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
	
	volaVol = p1.parameter1(volume)
	volaVal = p2.parameter2(value)
	buyTenDayLinreg = p3.parameter3(value)
	buyLinreg = p4.parameter4(value)

	pars = (([volaVol, volaVal, buyTenDayLinreg, buyLinreg]))

#	print("P1 THOURHG P4\n")
#	print( volaVol, volaVal, buyTenDayLinreg, buyLinreg)

	return pars

        #Probably should return all params as a list for easy writing to file
	#return volParam

#fileListSP = glob.glob("Data/*.csv")
#fileListVol = glob.glob("VolData/*.csv")

# List all files in the Data Directory
fileListSP = glob.glob("studentData/*.csv")

openFile = open(r"studentParams.txt", "w")

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
'''
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
'''
openFile.close()

sys.exit()
