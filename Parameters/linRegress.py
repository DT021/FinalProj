import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def avg(pList):

        aver = pList[-1]

        for i in range(len(pList) - 1):

                aver += pList[i]

        aver = aver / len(pList)

        return aver

def parMain(fileName):

        colnames = ['date', 'value', 'high', 'low', 'open', 'close', 'volume', 'adjClose']
        csvFile = pd.read_csv(fileName, names = colnames, skiprows = 1)
        value = csvFile.value.tolist()
        volume = csvFile.volume.tolist()

        return value


def linRegress(pList):

	w, h = 1, len(pList)

	xx = [[0 for x in range(w)] for y in range(h)] 

	count = 0

	for i in range(len(pList)):
		count = count + 1

		xx[i][0] = count

#	print(xx)
#	print(pList)

	model = LinearRegression().fit(xx, pList)

	return model.coef_

valList = parMain("Data/AIG20180701_20190101.csv")

hold = np.array(([10,7,3]))

average = avg(hold)
#print(average)

slope = linRegress(valList)

#print(slope)

