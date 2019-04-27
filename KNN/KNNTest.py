import KNN
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn import neighbors
import sys

openTrain = open("Parameters/trainParams.txt", "r")
openTest = open("Parameters/testParams.txt", "r")

# Read all of the training data
allLines = openTrain.readlines()

count = 0
for line in allLines:
    line = line.strip()
    param1, param2, param3, param4, classification = line.split(" ")

    # Read the end of file indicator to know the next data incoming is from trainParams.txt
    if param1 == "777":
        break
    # Load the training data trains for use
    if count == 0:
        xTrain = np.array([float(param1), float(param2), float(param3), float(param4)])
        yTrain = np.array([classification])
    else:
        newRow = np.array([float(param1), float(param2), float(param3), float(param4)])
        xTrain = np.vstack([xTrain, newRow])
        yTrain = np.append(yTrain, classification)

    count = count + 1

# Read all of the testing data
allLines = openTest.readlines()

count = 0
for line in allLines:
    line = line.strip()
    param1, param2, param3, param4, classification = line.split(" ")
    
    # Load the testing data train for use
    if count == 0:
        xTest = np.array([float(param1), float(param2), float(param3), float(param4)])
        trues = np.array([classification])
    else:
        newRow = np.array([float(param1), float(param2), float(param3), float(param4)])
        xTest = np.vstack([xTest, newRow])
        newTrue = np.array([classification])
        trues = np.vstack([trues, newTrue])

    count = count + 1

k = int(sys.argv[1])

# Call our python KNN implementation
ourClass = KNN.KNNClassifier(xTrain, yTrain, k)
ourPred = ourClass.classify(xTest)

# Call the scikit KNN implementation
scikitImp = neighbors.KNeighborsClassifier(k)
scikitImp.fit(xTrain, yTrain)
scikitPred = scikitImp.predict(xTest)

#Determine accuracy of all algorithm implementations based on percent error in classifications
ourError = 0
scikitError = 0
total = len(trues)

for i in range(total):

	if ourPred[i] != trues[i]:
		ourError += 1

	if scikitPred[i] != trues[i]:
		scikitError +=  1

print("Python Percent Error: ", float(ourError)/float(total) * 100)
print("Scikit Percent Error: ", float(scikitError)/float(total) * 100)

openTrain.close()
openTest.close()
