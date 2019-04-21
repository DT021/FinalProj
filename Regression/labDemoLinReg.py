import linReg
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

x = []
y = []

with open("test-data", "r") as data:
	for line in data:
		x.append(float(line.split(" ")[0]))
		y.append(float(line.split(" ")[1].strip()))

x = np.array((x[-180:]))
y = np.array((y[-180:]))

m, b = linReg.linReg(x, y)
pyRegY = m * x + b

cppRegY = np.zeros(x.size)

with open("cpp-reg-data.txt", "r") as cppData:
	i = 0
	for line in cppData:
		cppRegY[i] = float(line.split(" ")[1].strip())
		i += 1

sciReg = linear_model.LinearRegression()
sciReg.fit(x.reshape(-1, 1), y)
sciRegY = sciReg.predict(x.reshape(-1, 1))

results = {"pyReg":pyRegY, "cppReg":cppRegY, "sciReg":sciRegY}

for key in results:
	print(key, "Data:")
	print("\tR2:", r2_score(y, results[key]))
	print("\tMean Squared Error:", mean_squared_error(y, results[key]))

plt.plot(x, y)
plt.plot(x, pyRegY, color="blue", label="pyRegData")
plt.plot(x, cppRegY, color="red", label="cppRegData")
plt.plot(x, sciRegY, color="green", label="sciRegData")
plt.legend()
plt.title("Our Regression vs. Sci-Kit for 6 Months of Walmart Stocks")
plt.show()