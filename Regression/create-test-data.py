highs = []

with open ("../first_yahoo_prices_volumes_to_csv_demo.csv", "r") as file:
	for line in file:
		highs.append(line.split(",")[1])

with open("test-data", "w") as testData:
	for i in range(1, len(highs)):
		print(str(i - 1) + "," + highs[i], file=testData)

