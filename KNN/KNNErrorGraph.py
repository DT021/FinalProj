import matplotlib.pyplot as plt

k = []
cppError = []
pyError = []
sciKitError = []

with open("kError.txt", "r") as file:

	for line in file:
		data = line.split(" ")
		data[-1].strip()

		k.append(int(data[0]))
		cppError.append(float(data[1]))
		pyError.append(float(data[2]))
		sciKitError.append(float(data[3]))

plt.figure()
plt.plot(k, cppError, label="C++ Error", color="blue")
plt.plot(k, pyError, label="Python Error", color="green")
plt.plot(k, sciKitError, label="Scikit Error", color="red")
plt.title("Percent Error vs. K")
plt.legend()
plt.xlabel("Value of K")
plt.ylabel("Percent Error")
plt.show()