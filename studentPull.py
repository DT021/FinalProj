from KNN import KNN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import pandas_datareader as web
import parMain
import datetime
import sys

sYear, sMonth, sDay = 2018, 10, 25
eYear, eMonth, eDay = 2019, 4, 25

startDate = datetime.datetime(int(sYear), int(sMonth), int(sDay))
endDate = datetime.datetime(int(eYear), int(eMonth), int(eDay))

knownParams = []
knownClasses = []

# Load known classification data.
with open("demoTrain.txt", "r") as data:

	for line in data:
		knownParams.append(line.split(" ")[1:-1])
		knownClasses.append(line.split(" ")[-1].strip())

knownParams = np.array((knownParams), dtype="float32")
knownClasses = np.array((knownClasses))
knnClass = KNN.KNNClassifier(knownParams, knownClasses)

while True:
	ticker = input("Input a stock ticker: ")

	# Collect data for ticker and save to csv file.
	df = web.DataReader(ticker, 'yahoo', startDate, endDate)
	fileName = "studentData/test.csv"
	df.to_csv(fileName)

	# Determine parameters for chosen stock.
	studentParams = np.array(([parMain.parMain(fileName)[1:]]))
	prediction = knnClass.classify(studentParams)[0]

	print("Class Prediction:", prediction)

	# Graph known data with a color code. Graph chosen stock's data.
	colors = {"Volatile-Loss":"red", "Volatile-Gain":"yellow", "Stable-Gain":"green", "Stable-Loss":"orange"}
	fig = plt.figure()
	graph = fig.add_subplot(111, projection="3d")

	for i in range(knownClasses.shape[0]):
		currColor = colors[knownClasses[i]]
		graph.scatter(knownParams[i][0], knownParams[i][1], knownParams[i][2], color=currColor)

	graph.scatter(studentParams[0][0], studentParams[0][1], studentParams[0][2], color="purple")

	graph.set_xlabel("Volatility")
	graph.set_ylabel("Moving Avg Slope")
	graph.set_zlabel("Overall Slope")
	plt.show()