# File to clean large amounts of data and preprocess the points

# Courtesy of Red Gate Software Tutorial on using the Yahoo Stock API

#import external pandas_datareader library with alias of web
import pandas_datareader as web
 
#import datetime internal datetime module
#datetime is a Python module
import datetime
 
#datetime.datetime is a data type within the datetime module yy/mm/dd

# Get user input
ticker = input("Input company ticker\n")
sYear, sMonth, sDay  = map(int, input("Input start date yyyy mm dd\n").split())
eYear, eMonth, eDay = map(int, input("Input end date yyyy mm dd\n").split())

startDate = datetime.datetime(sYear, sMonth, sDay)
endDate = datetime.datetime(eYear, eMonth, eDay)
 
#DataReader method name is case sensitive
df = web.DataReader(ticker, 'yahoo', startDate, endDate)
 
#invoke to_csv for df dataframe object from 
#DataReader method in the pandas_datareader library
 
#..\first_yahoo_prices_to_csv_demo.csv must not
#be open in another app, such as Excel

df.to_csv('testWMT00_18.csv')

# Test reading line titles
# CSV reading info courtesy of realpython.com

import csv

pre_allocated_list = [None] * size

with open('testWMT00_18.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
#       else:
#            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#            line_count += 1
    print(f'Processed {line_count} lines.')
