"""The purpose of this script is to perform simple linear regression on Walmart 
stock prices to determine the average growth over time."""

import numpy as np
import matplotlib.pyplot as plt
from linReg import *
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error

days = []
highs = []

with open("test-data", "r") as data:
	for line in data:
		days.append(float(line.split(" ")[0].strip()))
		highs.append(float(line.split(" ")[1].strip()))

n = len(days[-180:])
x = np.array((days[-180:]))
yTrain = np.array((highs[-180:]))

m, b = linReg(x, yTrain)
y = m * x + b
R2 = calcR2(yTrain, y)

skReg = linear_model.LinearRegression()
skReg.fit(x.reshape(-1, 1), yTrain.reshape(-1, 1))
skPred = skReg.predict(x.reshape(-1, 1))

print(r2_score(yTrain, skPred))
print("Slope:", m)
print("R2:", R2)
print("Average Error:", mean_squared_error(yTrain, y))
print("Sklearn Average Error:", mean_squared_error(yTrain, skPred))

plt.title("Walmart Stock Price vs Python Prediction")
plt.text(1600, 80, "R^2 = " + str(round(R2, 4)))
plt.plot(x, yTrain)
plt.plot(x, y, label="Python Prediction", color="purple")
plt.plot(x, skPred, color="yellow")
plt.xlabel("Days since Start of Data")
plt.ylabel("Stock Price ($)")
plt.show()