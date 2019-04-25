import KNN
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn import neighbors

"""
iris = datasets.load_iris()
testSlice = -30
xTrain = iris.data[:testSlice][...,:3]
xTest = iris.data[testSlice:][...,:3]
yTrain = iris.target[:testSlice]

irisClass = KNN.KNNClassifier(xTrain, yTrain, k=3)
ourPred = irisClass.classify(xTest)

scikitIris = neighbors.KNeighborsClassifier()
scikitIris.fit(xTrain, yTrain)
scikitPred = scikitIris.predict(xTest)

actuals = iris.target[testSlice:]

#Determine accuracy of algorithm
ourCorrect = 0
scikitCorrect = 0
total = ourPred.size

for i in range(total):

	if ourPred[i] == actuals[i]:
		ourCorrect += 1

	if scikitPred[i] == actuals[i]:
		scikitCorrect += 1

# print("Our Accuracy:", (ourCorrect / total) * 100, "percent")
# print("Scikit Accuracy:", (scikitCorrect / total) * 100, "percent")
"""

#openTrain = open(r"../Parameters/train.txt", "r")
#openTest = open(r"../Parameters/test.txt", "r")
openTrain = open("../Parameters/train.txt", "r")
openTest = open("../Parameters/test.txt", "r")


allLines = openTrain.readlines()

count = 0
for line in allLines:
    line = line.strip()
    param1, param2, param3, param4, classification = line.split(" ")
    if param1 == "777":
        break
    if count == 0:
        xTrain = np.array([float(param1), float(param2), float(param3), float(param4)])
        yTrain = np.array([classification])
    else:
        newRow = np.array([float(param1), float(param2), float(param3), float(param4)])
        xTrain = np.vstack([xTrain, newRow])
        yTrain = np.append(yTrain, classification)

    count = count + 1

allLines = openTest.readlines()

count = 0
for line in allLines:
    line = line.strip()
    param1, param2, param3, param4, classification = line.split(" ")
    if count == 0:
        xTest = np.array([float(param1), float(param2), float(param3), float(param4)])
        trues = np.array([classification])
    else:
        newRow = np.array([float(param1), float(param2), float(param3), float(param4)])
        xTest = np.vstack([xTrain, newRow])
        trues = np.append(yTrain, classification)

    count = count + 1


ourClass = KNN.KNNClassifier(xTrain, yTrain, k=5)
ourPred = ourClass.classify(xTest)

scikitImp = neighbors.KNeighborsClassifier()
scikitImp.fit(xTrain, yTrain)
scikitPred = scikitImp.predict(xTest)

#Determine accuracy of algorithm
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

#print(xTrain)
#print(yTrain)
#print(xTest)
#print(trues)

openTrain.close()
openTest.close()