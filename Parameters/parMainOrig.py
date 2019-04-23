import pandas as pd
import parameter1 as p1
import glob

def parMain(fileName):

        colnames = ['date', 'value', 'high', 'low', 'open', 'close', 'volume', 'adjClose']
#        csvFile = pd.read_csv('../Data/'+fileName, names = colnames, skiprows = 1)
        csvFile = pd.read_csv(fileName, names = colnames, skiprows = 1)
        date = csvFile.date.tolist()
        value = csvFile.value.tolist()
        high = csvFile.high.tolist()
        low = csvFile.low.tolist()
        open = csvFile.open.tolist()
        close = csvFile.close.tolist()
        volume = csvFile.volume.tolist()
        adjClose = csvFile.adjClose.tolist()

        volParam = p1.parameter1(volume)

#        print("CHECK1")

        # Probably should return all params as a list for easy writing to file
        return volParam


fileListSP = glob.glob("Data/*.csv")
fileListVol = glob.glob("VolData/*.csv")

# List all files in the Data Directory
#fileListSP = glob.glob("../Data/*.csv")
#fileListVol = glob.glob("../VolData/*.csv")

openFile = open(r"params.txt", "a")

print("for loop before")
for fileName in fileListSP:
#    print("CHECK2")
    paramsSP = parMain(fileName)
    L = [str(paramsSP), " Non-volatile\n"]
    openFile.writelines(L)

for fileName in fileListVol:
#    print("CHECK3")
    paramsVol = parMain(fileName)
    L = [str(paramsVol), " Volatile\n"]
    openFile.writelines(L)

openFile.close()
