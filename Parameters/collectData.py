"""
This program calls parMain.py for all stock tickers and then writes all four parameters and a classification to the params.txt file 
"""

import glob
import parMain

fileListSP = glob.glob("Data/*.csv")
fileListVol = glob.glob("VolData/*.csv")
openFile = open("Parameters/params.txt", "w")

count = 0

for fileName in fileListSP:	
    """Calls all stocks from the S&P500 tickers"""
    # count = count + 1
    # print(count)
	
    parsSP = parMain.parMain(fileName)

    volTotal = parsSP[0] + parsSP[1]
    valTotal = parsSP[2] + parsSP[3]

    if (volTotal > 4) and (valTotal > 0):
        L = [str(parsSP[0]), " ", str(parsSP[1]), " ", str(parsSP[2][0]), " ", str(parsSP[3][0]), " Volatile-Gain", "\n"]
    elif (volTotal > 4) and (valTotal <= 0):
        L = [str(parsSP[0]), " ", str(parsSP[1]), " ", str(parsSP[2][0]), " ", str(parsSP[3][0]), " Volatile-Loss", "\n"]
    elif (volTotal < 4) and (valTotal > 0):
        L = [str(parsSP[0]), " ", str(parsSP[1]), " ", str(parsSP[2][0]), " ", str(parsSP[3][0]), " Stable-Gain", "\n"]
    elif (volTotal < 4) and (valTotal <= 0):
        L = [str(parsSP[0]), " ", str(parsSP[1]), " ", str(parsSP[2][0]), " ", str(parsSP[3][0]), " Stable-Loss", "\n"]

    openFile.writelines(L)

count = 0

for fileName in fileListVol:
	"""Calls all stocks from the volatile stocks list"""
        # count = count + 1
        # print(count)

        parsVol = parMain.parMain(fileName)

        volTotal = parsVol[0] + parsVol[1]
        valTotal = parsVol[2] + parsVol[3]

        if (volTotal > 4) and (valTotal > 0):
            L = [str(parsVol[0]), " ", str(parsVol[1]), " ", str(parsVol[2][0]), " ", str(parsVol[3][0]), " Volatile-Gain", "\n"]
        elif (volTotal > 4) and (valTotal <= 0):
            L = [str(parsVol[0]), " ", str(parsVol[1]), " ", str(parsVol[2][0]), " ", str(parsVol[3][0]), " Volatile-Loss", "\n"]
        elif (volTotal < 4) and (valTotal > 0):
            L = [str(parsVol[0]), " ", str(parsVol[1]), " ", str(parsVol[2][0]), " ", str(parsVol[3][0]), " Stable-Gain", "\n"]
        elif (volTotal < 4) and (valTotal <= 0):
            L = [str(parsVol[0]), " ", str(parsVol[1]), " ", str(parsVol[2][0]), " ", str(parsVol[3][0]), " Stable-Loss", "\n"]

        openFile.writelines(L)

openFile.close()
