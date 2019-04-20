def parameter1( volList ):

	avg = volList[-1]
	volaAvg = 0

	for i in range(len(volList) - 1):
		volaAvg += abs( volList[i] - (volList[i + 1]) )
		
		avg += volList[i]
		
	avg = avg / len(volList)
	volaAvg	= volaAvg / (len(volList) - 1)

	volaPercent = volaAvg / avg	

	return volaPercent

