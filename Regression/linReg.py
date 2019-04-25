import matplotlib.pyplot as plt
import numpy as np

class LinearRegression():

	def __init__(self, xTrain, yTrain):
		self.xTrain = np.array((xTrain))
		self.yTrain = np.array((yTrain))
		self.slope = 0
		self.yInter = 0

	def fitData(self, alpha=0.0000001, epochs=10000):
		"""Fit data to a linear model. Save y intercept and slope to class."""

		n = self.xTrain.shape[0]
		self.slope = 0
		self.yInter = 0

		for epoch in range(epochs):
			yTest = self.slope * self.xTrain + self.yInter
			error = yTest - self.yTrain

			# Adjust slope and y intercept in opposite dirrection of error gradient.
			self.slope -= alpha * 2 * np.sum(error * self.xTrain) / n
			self.yInter -= alpha * 2 * np.sum(error) / n

	def predict(self, xTest):
		"""Given a set of x values, predict corresponding y values with the 
		determined linear model and return them in a numpy array."""

		return self.slope * xTest + self.yInter

	def addData(self, newX, newY):

		self.xTrain = np.concatenate(self.xTrain, newX)
		self.yTrain = np.concatenate(self.yTrain, newY)

	def resetData(self, newX=np.array(([])), newY=np.array(([]))):
		"""Change data to given data. Clears arrays by default."""

		self.xTrain = newX
		self.yTrain = newY

	def graphLine(self):
		"""Graph the linear model and the given data."""

		plt.plot(self.xTrain, self.yTrain, label="Actual Data")
		plt.plot(self.xTrain, self.slope * self.xTrain + self.yInter, label="Linear Model")
		plt.title("Linear Model vs. Actual Data")
		plt.legend()
		plt.show()

def calcR2(y, yTest):
	ssRes = np.sum((y - yTest) ** 2)
	ssTot = np.sum((y - np.sum(y)/len(y)) ** 2)

	R2 = 1 - ssRes / ssTot

	return R2

def calcAvgError(y, yTest):
	return np.average(np.sqrt((y - yTest) ** 2))

"""x = np.arange(100)
y = np.linspace(0, 50, 100)

linTest = LinearRegression(x, y)
linTest.fitData()
linTest.graphLine()

linTest.resetData(np.linspace(0, 50), np.linspace(120, 50, 50))
linTest.fitData(epochs=100000, alpha=0.0001)
linTest.graphLine()"""
