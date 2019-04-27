import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class KMeansCluster():

	def __init__(self, data):
		self.data = data
		self.groups = np.zeros(data.shape[0], dtype='int32')
		self.groupCenters = np.array([])

	def addData(self, newData):
		"""Append newData to self.data
		"""

		self.data = np.concatenate((self.data, newData))

	def resetData(self, newData=np.array(([]))):
		"""Replace data with given data set. Clears self.data by default.
		"""

		self.data = newData

	def cluster(self, numGroups, epochs=10000, maxRand=1, minRand=0, logEpochs=False):
		"""Determine the center points of any 'groups' found in the data set."""

		self.groupCenters = np.random.rand(numGroups, self.data.shape[1]) * (maxRand - minRand) + minRand
		
		for epoch in range(epochs):
			groupPoints = []

			for group in range(numGroups):
				groupPoints.append([])

			# Calculate distance from each point to each group center.
			for i in range(self.data.shape[0]):
				distances = []
				distance = 0

				for j in range(self.groupCenters.shape[0]):
					distance = 0

					for k in range(self.data[i].shape[0]):
						distance += (self.data[i][k] - self.groupCenters[j][k]) ** 2

					distance = math.sqrt(distance)
					distances.append([j, distance])

				# Set point's group to closest group center
				group = sorted(distances, key=lambda elem: elem[1])[0][0]
				self.groups[i] = group
				# Add point vector to group list for later averaging.
				groupPoints[group].append(self.data[i])

			# Change group centers to average of all vectors belonging to that group.
			for j in range(numGroups):
				points = groupPoints[j]
				pointSum = 0

				for k in range(self.data.shape[1]):
					pointSum = 0

					for point in points:
						pointSum += point[k]

					if (len(points) != 0):
						self.groupCenters[j][k] = pointSum / len(points)

	def graphData(self):
		"""Use matplotlib to display the data and calculated group centers."""

		colors = ["blue", "green", "purple"]

		for i in range(self.data.shape[0]):
			plt.scatter(self.data[i][0], self.data[i][1], color=colors[self.groups[i]])

		plt.scatter(self.groupCenters[...,0], self.groupCenters[...,1], color="red")

		plt.show()


class KNNClassifier():

	def __init__(self, xTrain, yTrain, k=5):
		"""
		xTrain = 2D numpy array
		yTrain = 1D numpy array
		k = int
		"""
		self.xTrain = xTrain
		self.yTrain = yTrain
		self.k = int(k)
		self.classifications = []
		self.getClassifications()

	def getClassifications(self):

		for classification in self.yTrain:

			if classification not in self.classifications:
				self.classifications.append(classification)

	def addData(self, newX, newY):
		""" Append data to xTrain and yTrain """

		self.xTrain = np.concatenate((self.xTrain, newX))
		self.yTrain = np.concatenate((self.yTrain, newY))
		self.getClassifications()

	def clearData(self, newX=np.array([[]]), newY=np.array([])):
		""" Replace xTrain and yTrain with newX and newY. Resets original
		arrays by default"""

		self.xTrain = newX
		self.yTrain = newY

	def classify(self, x):
		""" Classify a given array of independent variables. Return a 1D numpy 
		array of the results. x must be a 2D numpy array of shape (n, 1)."""

		predictions = np.zeros(x.shape[0], self.yTrain.dtype)

		votes = {}

		# Calculate Euclidian distance from every test point to every training 
		# point.
		for i in range(x.shape[0]):
			distances = []

			for classification in self.classifications:
				votes[classification] = 0

			# Compare each test point to each training point.
			for j in range(self.xTrain.shape[0]):
				distance = 0

				# Calculate distance on each each axis.
				for k in range(self.xTrain[0].size):
					distance += (x[i][k] - self.xTrain[j][k]) ** 2

				distance = math.sqrt(distance)
				distances.append([distance, self.yTrain[j]])

			distances = sorted(distances, key=lambda elem: elem[0])

			for neighb in range(self.k):
				votes[distances[neighb][1]] += 1

			# Set prediction to highest voted type.
			predictions[i] = sorted(votes.items(), key=lambda vote: vote[1], reverse=True)[0][0]

		return np.array((predictions))


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