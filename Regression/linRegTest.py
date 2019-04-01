"""The purpose of this script is to perform simple linear regression on Walmart 
stock prices to determine the average growth over time."""

import numpy as np
import matplotlib.pyplot as plt
from linReg import *

days = []
highs = []

with open("test-data", "r") as data:
	for line in data:
		days.append(float(line.split(" ")[0].strip()))
		highs.append(float(line.split(" ")[1].strip()))

n = len(days[1500:])
x = np.array((days[1500:]))
yTrain = np.array((highs[1500:]))

m, b = linReg(x, yTrain)
y = m * x + b
R2 = calcR2(yTrain, y)

print("Slope:", m)
print("R2:", R2)

plt.title("Walmart Stock Price vs Python Prediction")
plt.text(1600, 80, "R^2 = " + str(round(R2, 4)))
plt.plot(x, yTrain)
plt.plot(x, y, label="Python Prediction", color="purple")
plt.xlabel("Days since Start of Data")
plt.ylabel("Stock Price ($)")
plt.show()