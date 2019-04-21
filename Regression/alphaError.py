import matplotlib.pyplot as plt

alphas = []
avgErrors = []

with open("alphaErrorData.txt", "r") as data:

	for line in data:

		alphas.append(float(line.split(" ")[0]))
		avgErrors.append(float(line.split(" ")[1].strip()))

start = 300
end = 330

plt.plot(alphas[start:end], avgErrors[start:end], color="red", label="Average Error")
plt.legend()
plt.title("Average Error as a Function of Learning Rate")
plt.show()