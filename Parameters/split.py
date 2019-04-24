openFile = open(r"params.txt", "r")
allLines = openFile.readlines()

trainFile = open(r"train.txt", "a")
testFile = open(r"test.txt", "a")

for i in range(0, len(allLines)):
        
        if i%10 < 7:
            
            trainFile.write(allLines[i])

        else:

            testFile.write(allLines[i])

trainFile.write("777 0 0 0 0\n")

openFile.close()
trainFile.close()
testFile.close()

