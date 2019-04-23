# This parameter is price volatility measure.
# It is the average change between days divided by the average price

def parameter2( priceList ):

        avg = priceList[-1]
        volaAvg = 0

        for i in range(len(priceList) - 1):
                volaAvg += abs( priceList[i] - (priceList[i + 1]) )

                avg += priceList[i]

        avg = avg / len(priceList)
        volaAvg = volaAvg / (len(priceList) - 1)

        volaPercent = volaAvg / avg

        return volaPercent
