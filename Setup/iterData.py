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
 
        fileName = ticker + sYear + sMonth + sDay + '_' + eYear + eMonth + eDay + '.csv'
	
	#Data file to CSV
        df.to_csv('VolData/'+fileName)

        lineCount = lineCount + 1

    line = file.readline()

file.close()
