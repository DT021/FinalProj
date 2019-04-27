# This script pulls our list of S&P Tickers from the yahoo stock API and loads them into a series of .csv files

import pandas as pd
import pandas_datareader as web
import datetime
import sys

# Open the command line inputted file of date and tickers
file = open(sys.argv[1])

lineCount = 0

line = file.readline()

while line:

    if lineCount == 0:

        # Get user input for date
        sYear, sMonth, sDay, eYear, eMonth, eDay = line.split()

        startDate = datetime.datetime(int(sYear), int(sMonth), int(sDay))
        endDate = datetime.datetime(int(eYear), int(eMonth), int(eDay))

        lineCount = lineCount + 1

    else:

        # Yank endlines
        ticker = line.replace('\n','') 

        print(ticker)
        print("\n")

        # Pull from the stock API
        df = web.DataReader(ticker, 'yahoo', startDate, endDate)
 
        # Invoke to_csv for df dataframe object from DataReader method in the pandas_datareader library
 
        # ..\first_yahoo_prices_to_csv_demo.csv must not be open in another app, such as Excel
        
        fileName = ticker + sYear + sMonth + sDay + '_' + eYear + eMonth + eDay + '.csv'

#        df.to_csv('testWMT00_18.csv')
#        df.to_csv('Data/'+fileName)
        df.to_csv('VolData/'+fileName)

        # Test reading lines

#        colnames = ['date', 'value', 'high', 'low', 'open', 'close', 'volume', 'adjClose']
#        csvFile = pd.read_csv('Data/'+fileName, names = colnames, skiprows = 1)

#        date = csvFile.date.tolist()
#        value = csvFile.value.tolist()
#        high = csvFile.high.tolist()
#        low = csvFile.low.tolist()
#        open = csvFile.open.tolist()
#        close = csvFile.close.tolist()
#        volume = csvFile.volume.tolist()
#        adjClose = csvFile.adjClose.tolist()

        lineCount = lineCount + 1

    line = file.readline()

file.close()

# How to strip last character
#line = file.readline()
#line = line[:-1]
