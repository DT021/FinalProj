import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

class KMeansCluster():

	def __init__(self, data):
		self.data = data

	def addData(self, newData):
		"""Append newData to self.data
		"""

		self.data = np.concatenate((self.data, newData))

	def resetData(self, newData=np.array(([]))):
		"""Replace data with given data set. Clears self.data by default.
		"""

		self.data = newData

	def cluster(self, numGroups, epochs=10000, maxRand=1, minRand=0):

		groupCenters = np.random.rand(numGroups, self.data.shape[1]) * maxRand
		
		for i in range(epochs):
			groupPoints = []

			for group in range(numGroups):
				groupPoints.append([])

			# Calculate distance from each point to each group center.
			for point in self.data:
				distances = []
				distance = 0

				for j in range(groupCenters.shape[0]):
					distance = 0

					for k in range(point.shape[0]):
						distance += (point[k] - groupCenters[j][k]) ** 2

					distance = math.sqrt(distance)
					distances.append([j, distance])

				# Set point's group to closest group center
				group = sorted(distances, key=lambda elem: elem[1])[0][0]
				#print(group)
				# Add point vector to group list for later averaging.
				groupPoints[group].append(point)

			# Change group centers to average of all vectors belonging to that group.
			for j in range(numGroups):
				break

iris = datasets.load_iris()
kmeans = KMeansCluster(iris.data)
kmeans.cluster(3, epochs=1, maxRand=5)