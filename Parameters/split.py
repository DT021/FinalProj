# Split the total data params.txt file into a trainParams.txt and a test.txt 

openFile = open(r"Parameters/params.txt", "r")
allLines = openFile.readlines()

trainFile = open(r"Parameters/trainParams.txt", "w")
testFile = open(r"Parameters/testParams.txt", "w")

for i in range(0, len(allLines)):
        
        if i%10 < 7:
            
            trainFile.write(allLines[i])

        else:

            testFile.write(allLines[i])

trainFile.write("777 0 0 0 0\n")

openFile.close()
trainFile.close()
testFile.close()

