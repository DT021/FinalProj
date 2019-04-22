import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets, neighbors

iris = datasets.load_iris()
testSlice = -30
xTrain = iris.data[:testSlice][...,:3]
xTest = iris.data[testSlice:][...,:3]
yTrain = iris.target[:testSlice]

scikitIris = neighbors.KNeighborsClassifier()
scikitIris.fit(xTrain, yTrain)
scikitPred = scikitIris.predict(xTest)

actuals = iris.target[testSlice:]

openFile = open(r"irisTrain.txt","a")

for i in range(len(yTrain)):
    L = [str(xTrain[i,0]), " ",  str(xTrain[i,1]), " ", str(xTrain[i,2]), " ", str(yTrain[i]), "\n"]
    openFile.writelines(L)

L = [str(777), " ", str(0), " ", str(0), " ", str(0), "\n"]
openFile.writelines(L)

openFile.close()

openFile = open(r"irisTest.txt", "a")

for i in range(len(xTest)):
    L = [str(xTest[i,0]), " ", str(xTest[i,1]), " ", str(xTest[i,2]), "\n"]
    openFile.writelines(L)

openFile.close()
