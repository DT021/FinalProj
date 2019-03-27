"""The purpose of this script is to perform simple linear regression on Walmart 
stock prices to determine the average growth over time."""

import numpy as np

def calcR2(y, yTest):
	ssRes = np.sum((y - yTest) ** 2)
	ssTot = np.sum((y - np.sum(y)/len(y)) ** 2)

	R2 = 1 - ssRes / ssTot

	return R2

def linReg(x, y, alpha=0.0000001, epochs=10000):
	"""Return the slope, y intercept and R2 of a regression line 
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

	return m, b, calcR2(y, yTest)