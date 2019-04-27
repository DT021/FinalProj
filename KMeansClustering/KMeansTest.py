# Print time elapsed for python implementation and scikit.

import KMeans
import numpy as np
import time
from sklearn.cluster import KMeans
from sklearn import datasets
import sys

iris = datasets.load_iris()
testSlice = -30
xTrain = iris.data[:-30][...,:3]

irisCluster = KMeans.KMeansCluster(xTrain)
k = sys.argv[1]
start = time.time()
irisCluster.cluster(k, epochs=100)
finish = time.time() - start
print finish * (10 ** 6), "\n"

start = time.time()
sciCluster = KMeans(n_clusters=k)
sciCluster.fit()
finish = time.time() - start
print finish * (10 ** 6), "\n"