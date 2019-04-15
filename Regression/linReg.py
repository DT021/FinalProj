"""The purpose of this script is to perform simple linear regression on Walmart 
stock prices to determine the average growth over time."""

import numpy as np

def calcR2(y, yTest):
	ssRes = np.sum((y - yTest) ** 2)
	ssTot = np.sum((y - np.sum(y)/len(y)) ** 2)

	R2 = 1 - ssRes / ssTot

	return R2

def calcAvgError(y, yTest):
	return np.average(np.sqrt((y - yTest) ** 2))

def linReg(x, y, alpha=0.0000001, epochs=10000):
	"""Return the slope and y intercept of a regression line 
	built on the given data.
	
	x, y = np float arrays
	alpha = float
	epochs = int
	"""

	n = len(x)
	m, b = 0, 0

	for i in range(epochs):

		yTest = m * x + b
		error = yTest - y

		# Adjust slope and y intercept based on error gradient.
		m -= alpha * 2 * np.sum(error * x) / n
		b -= alpha * 2 * np.sum(error) / n

	return m, b