import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn import datasets

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