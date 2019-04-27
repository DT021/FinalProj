import matplotlib.pyplot as plt

k = []
cppError = []
pyError = []
scikitError = []

with open("KMCTiming.txt", "r") as file:

	for line in file:
		data = [x.strip() for x in line.split(" ")]

		k.append(int(data[0]))
		cppError.append(float(data[1]))
		pyError.append(float(data[2]))
		scikitError.append(float(data[3]))

plt.figure()
plt.plot(k, cppError, label="C++ Time", color="blue")
plt.plot(k, pyError, label="Python Time", color="green")
plt.plot(k, scikitError, label="Scikit Time", color="red")
plt.title("Time Elapsed vs. K")
plt.legend()
plt.xlabel("K Value")
plt.ylabel("Time Elapsed (microseconds)")
plt.show()