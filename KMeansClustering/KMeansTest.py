# Print time elapsed for python implementation and scikit.

import numpy as np
import time
from KMeans import KMeansCluster
from sklearn.cluster import KMeans as KMC
from sklearn import datasets
import sys

iris = datasets.load_iris()
testSlice = -30
xTrain = iris.data[:-30][...,:3]

k = int(sys.argv[1])

Cluster = KMeansCluster(xTrain)

start = time.time()
Cluster.cluster(int(k), 100)
finish = time.time() - start
print(finish * (10 ** 6), end=" ")

start = time.time()
sciCluster = KMC(n_clusters=k)
sciCluster.fit(xTrain)
finish = time.time() - start
print(finish * (10 ** 6))
