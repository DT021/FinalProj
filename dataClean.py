# Test File for Data Cleaning

# Courtesy of Red Gate Software Tutorial on using the Yahoo Stock API

#import external pandas_datareader library with alias of web
import pandas_datareader as web
 
#import datetime internal datetime module
#datetime is a Python module
import datetime
 
#datetime.datetime is a data type within the datetime module
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 1, 1)
 
#DataReader method name is case sensitive
df = web.DataReader("WMT", 'yahoo', start, end)
 
#invoke to_csv for df dataframe object from 
#DataReader method in the pandas_datareader library
 
#..\first_yahoo_prices_to_csv_demo.csv must not
#be open in another app, such as Excel
 
df.to_csv('first_yahoo_prices_volumes_to_csv_demo.csv')
