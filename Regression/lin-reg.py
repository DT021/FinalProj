"""The purpose of this script is to perform simple linear regression on Walmart 
stock prices to determine the average growth over time."""

import numpy as np

days = []
highs = []

with open("test-data", "r") as data:
	for line in data:
		days.append(float(line.split(",")[0].strip()))
		highs.append(float(line.split(",")[1].strip()))

"""n = len(days)
x = np.array((days))
yTrain = np.array((highs))"""
n = 100
x = np.arange(100)
yTrain = np.arange(100)

slope = 0
yInter = 0

def linReg(x, y, alpha=0.0000001, epochs=10000):
	"""Return the slope, y intercept and mean squared error of a regression line 
	built on the given data.
	
	x, y = np arrays
	alpha = float
	epochs = int
	"""

	n = len(x)
	m, b = 0, 0

	for i in range(epochs):

		yTest = m * x + b
		error = yTest - y

		m -= alpha * 2 * np.sum(error * x) / n
		b -= alpha * 2 * np.sum(error) / n

	mSqrErr = np.sum(error ** 2) / n

	return m, b, mSqrErr


m, b, err = linReg(x, yTrain)
print(m, b, err)

"""learningRate = 0.0000001
epochs = 10000

print(yTrain.shape)

for i in range(epochs):

	yTest = slope * x + yInter

	error = yTest - yTrain
	squareError = error * error
	meanSquareError = np.sum(squareError) / n

	slope = slope - learningRate * 2 * np.sum(error * x) / n
	yInter = yInter - learningRate * 2 * np.sum(error) / n

	#if (i % 1000) == 0:
		#print(meanSquareError)

print("regression line: y =", slope, "x +", yInter)
print(meanSquareError)"""