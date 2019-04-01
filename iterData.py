# File to clean large amounts of data and preprocess the points

# Courtesy of Red Gate Software Tutorial on using the Yahoo Stock API

import pandas as pd

# Import external pandas_datareader library with alias of web
import pandas_datareader as web
 
# Import datetime internal datetime module datetime is a Python module
import datetime
 
# Datetime.datetime is a data type within the datetime module yy/mm/dd

import sys

#with open(sys.argv[1]) as file:
#    fileContents = file.read()
#    print(fileContents)

file = open(sys.argv[1])

lineCount = 0

line = file.readline()

while line:

    if lineCount == 0:

        # Get user input
        sYear, sMonth, sDay, eYear, eMonth, eDay = line.split()

#        ticker = input("Input company ticker\n")
#        sYear, sMonth, sDay  = map(int, input("Input start date yyyy mm dd\n").split())
#        eYear, eMonth, eDay = map(int, input("Input end date yyyy mm dd\n").split())

        startDate = datetime.datetime(int(sYear), int(sMonth), int(sDay))
        endDate = datetime.datetime(int(eYear), int(eMonth), int(eDay))

        lineCount = lineCount + 1

    else:
 
        ticker = line.replace('\n','') 

        # DataReader method name is case sensitive
        df = web.DataReader(ticker, 'yahoo', startDate, endDate)
 
        # Invoke to_csv for df dataframe object from DataReader method in the pandas_datareader library
 
        # ..\first_yahoo_prices_to_csv_demo.csv must not be open in another app, such as Excel
        
        fileName = ticker + sYear + sMonth + sDay + '_' + eYear + eMonth + eDay + '.csv'

#        df.to_csv('testWMT00_18.csv')
        df.to_csv('Data/'+fileName)
        
        # Test reading lines

        colnames = ['date', 'value', 'high', 'low', 'open', 'close', 'volume', 'adjClose']
#        csvFile = pd.read_csv('testWMT00_18.csv', names=colnames, skiprows = 1)
        csvFile = pd.read_csv('Data/'+fileName, names = colnames, skiprows = 1)

        date = csvFile.date.tolist()
        value = csvFile.value.tolist()
        high = csvFile.high.tolist()
        low = csvFile.low.tolist()
        open = csvFile.open.tolist()
        close = csvFile.close.tolist()
        volume = csvFile.volume.tolist()
        adjClose = csvFile.adjClose.tolist()

        lineCount = lineCount + 1

    line = file.readline()

file.close()

# How to strip last character
#line = file.readline()
#line = line[:-1]
