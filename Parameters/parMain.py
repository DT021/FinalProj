import pandas as pd
import parameter1.py as p1


def parMain( fileName ):

        colnames = ['date', 'value', 'high', 'low', 'open', 'close', 'volume', 'adjClose']
        csvFile = pd.read_csv('../Data/'+fileName, names = colnames, skiprows = 1)

        date = csvFile.date.tolist()
        value = csvFile.value.tolist()
        high = csvFile.high.tolist()
        low = csvFile.low.tolist()
        open = csvFile.open.tolist()
        close = csvFile.close.tolist()
        volume = csvFile.volume.tolist()
        adjClose = csvFile.adjClose.tolist()



        return
