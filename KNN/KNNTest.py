import KNN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn import datasets, neighbors

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

print("Our Accuracy:", (ourCorrect / total) * 100, "percent")
print("Scikit Accuracy:", (scikitCorrect / total) * 100, "percent")