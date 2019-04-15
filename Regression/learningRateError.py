import linReg
import numpy as np

day = []
price = []

with open("test-data", "r") as data:
	for line in data:
		day.append(float(line.split(" ")[0]))
		price.append(float(line.split(" ")[1]))

x = np.array((day[-100:]))
y = np.array((price[-100:]))

xTrain = x[:70]
yTrain = y[:70]

xTest = x[-70:]
yTest = y[-70:]

slope, yInter = 0, 0
alpha = 0.00000021 # Maximum working alpha

with open("alphaErrorData", "w") as data:
	for i in range(1000):
		slope, yInter = linReg.linReg(xTrain, yTrain, alpha)
		y = slope * xTest + yInter

		print(alpha, linReg.calcAvgError(y, yTest), file=data)
		alpha -= 0.00000000001