import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn import datasets

class KMeansCluster():

	def __init__(self, data):
		self.data = data
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
		self.groupCenters = np.random.rand(numGroups, self.data.shape[1]) * maxRand
		
		for i in range(epochs):
			groupPoints = []

			for group in range(numGroups):
				groupPoints.append([])

			# Calculate distance from each point to each group center.
			for point in self.data:
				distances = []
				distance = 0

				for j in range(self.groupCenters.shape[0]):
					distance = 0

					for k in range(point.shape[0]):
						distance += (point[k] - self.groupCenters[j][k]) ** 2

					distance = math.sqrt(distance)
					distances.append([j, distance])

				# Set point's group to closest group center
				group = sorted(distances, key=lambda elem: elem[1])[0][0]
				#print(group)
				# Add point vector to group list for later averaging.
				groupPoints[group].append(point)

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
		pass



iris = datasets.load_iris()
kmeans = KMeansCluster(iris.data[...,:2])
kmeans.cluster(3, epochs=100, maxRand=5)
kmeans.graphData()